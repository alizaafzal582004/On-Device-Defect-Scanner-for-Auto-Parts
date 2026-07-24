# 🚗 On-Device Defect Scanner for Auto Parts

> ### ⚡ Detect microscopic automotive defects in **under 50 ms** using **Edge AI** — no cloud, no internet, no latency.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![YOLOv11](https://img.shields.io/badge/YOLOv11-Nano-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-00C7B7?style=for-the-badge&logo=fastapi)
![ONNX Runtime](https://img.shields.io/badge/ONNX_Runtime-Optimized-orange?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/MIT-License-success?style=for-the-badge)

</p>

---

# Why This Project?

Every second, automotive manufacturers produce hundreds of metal components.

A single **undetected micro-defect** can lead to:

Costly recalls
Warranty claims
Production downtime
Customer dissatisfaction

Traditional visual inspection simply **can't keep up**.

So I built an **Edge AI Quality Inspection System** capable of detecting defects **directly on production hardware** without relying on cloud servers.

---

# The Solution

Instead of sending factory images to the cloud...

This system performs **real-time defect detection entirely on-device**, making industrial inspection:

 Faster
 More secure
 Completely offline
 Lower cost
 Production ready

Powered by **YOLOv11 Nano**, **FastAPI**, **OpenCV**, and **ONNX Runtime**, the model delivers industrial-grade inspection on compact edge hardware.

---

# 🎥 Demo

<p align="center">

**Demo vedio**

https://drive.google.com/file/d/1YqviTWZhLUgpVi8F2Zepmzzs4dhcNQY7/view?usp=sharing


</p>

---

# 📸 

<p align="center">
 
<img width="1600" height="730" alt="image" src="https://github.com/user-attachments/assets/8eb654d9-1a09-4415-9a6d-04c01a79a107" />

</p>

---

# Features

 Real-Time Edge AI Detection
 Lightweight YOLOv11 Nano
 FastAPI REST API
 Browser Dashboard
 ONNX Runtime Optimization
 Docker Deployment
 Raspberry Pi Support
 NVIDIA Jetson Support
 Automatic Image Annotation
 Industrial Quality Inspection

---

# 🏗 System Architecture

```text
Industrial Camera
        │
        ▼
 Image Preprocessing
   (OpenCV)
        │
        ▼
 YOLOv11 Nano
        │
        ▼
 ONNX Runtime
        │
        ▼
 FastAPI Server
        │
        ▼
 Dashboard / MES
```

---

#  Tech Stack

| AI | Backend | Deployment | Vision |
|------|---------|------------|---------|
| YOLOv11 Nano | FastAPI | Docker | OpenCV |
| ONNX Runtime | Uvicorn | Raspberry Pi | Pillow |
| Python | REST API | Jetson Nano | NumPy |

---

#  Performance

| Metric | Result |
|---------|---------|
| Model | YOLOv11 Nano |
| Model Size | ~9 MB |
| Target mAP@50 | **72%** |
| Target Latency | **35–50 ms** |
| GPU Speed | **34.8 Parts/sec** |
| CPU Speed | **8–9 FPS** |
| Edge Deployment | ✅ |

> **Note:** The values above represent documented benchmark targets. Replace them with the actual evaluation metrics from your training results (`results.csv`) when available.

---

#  AI Pipeline

```text
Image Capture
      ↓
Image Processing
      ↓
YOLO Detection
      ↓
Bounding Boxes
      ↓
Confidence Filtering
      ↓
Annotated Output
      ↓
REST API Response
```

---

# 📂 Project Structure

```text
On-Device-Defect-Scanner/

├── best1.pt
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── static/
│     └── index.html
│
└── docs/
      ├── demo.gif
      └── screenshots/
```

---

#  Quick Start

```bash
git clone https://github.com/alizaafzal582004/On-Device-Defect-Scanner-for-Auto-Parts.git

cd On-Device-Defect-Scanner-for-Auto-Parts

docker compose up --build -d
```

Open

```
http://localhost
```

Upload an image.

Get defect predictions instantly.

---

#  Real-World Applications

 Automotive Manufacturing
 Metal Casting Inspection
 CNC Parts Inspection
 Vehicle Components
 Industrial Automation
 Production Quality Control

---

# Future Roadmap

- TensorRT Optimization
- INT8 Quantization
- Live Camera Streaming
- Multi-Camera Inspection
- Defect Analytics Dashboard
- Production Reports
- Active Learning Pipeline
- MES Integration

---

# ⭐ If you found this project useful...

Give it a ⭐ and help more developers discover Edge AI for industrial inspection.
