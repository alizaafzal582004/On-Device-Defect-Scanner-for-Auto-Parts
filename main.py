from contextlib import asynccontextmanager
from io import BytesIO

from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
from ultralytics import YOLO

MODEL_PATH = "best1.pt"

# This dict holds the model so it is loaded ONCE (at startup),
# not on every request -> fast + consistent responses.
ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- STARTUP: runs once, before the server accepts requests ----
    ml_models["yolo"] = YOLO(MODEL_PATH)
    print("Model loaded successfully.")
    yield
    # ---- SHUTDOWN: runs once, when the server stops ----
    ml_models.clear()


app = FastAPI(title="Bergwerk Autoparts - Edge AI Defect Scanner", lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running."}


@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    conf: float = Query(0.25, ge=0.01, le=0.99, description="Confidence threshold"),
):
    """
    Upload an image -> get back JSON with detected defects
    (class name, confidence, bounding box), filtered by the given
    confidence threshold.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes)).convert("RGB")

    model = ml_models["yolo"]
    results = model(image, conf=conf)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class_id": int(box.cls[0]),
                "class_name": model.names[int(box.cls[0])],
                "confidence": round(float(box.conf[0]), 4),
                "bbox_xyxy": [round(v, 2) for v in box.xyxy[0].tolist()],
            })

    return {"filename": file.filename, "confidence_threshold": conf, "detections": detections}


@app.post("/predict/image")
async def predict_image(
    file: UploadFile = File(...),
    conf: float = Query(0.25, ge=0.01, le=0.99, description="Confidence threshold"),
):
    """
    Upload an image -> get back the SAME image with bounding boxes
    drawn on it, filtered by the given confidence threshold.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes)).convert("RGB")

    model = ml_models["yolo"]
    results = model(image, conf=conf)

    annotated_array = results[0].plot()  # numpy array (BGR) with boxes drawn
    annotated_image = Image.fromarray(annotated_array[:, :, ::-1])  # BGR -> RGB

    buf = BytesIO()
    annotated_image.save(buf, format="JPEG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/jpeg")


# Serves the whole frontend (dashboard.html, scanner.html, reports.html,
# settings.html, css/, js/). html=True means visiting "/" serves index.html
# automatically -- so we point index.html at the dashboard.
# Mounted LAST so it never shadows the API routes above.
app.mount("/", StaticFiles(directory="static", html=True), name="static")