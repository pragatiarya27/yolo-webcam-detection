# yolo-webcam-detection
Real-time object detection using YOLOv8 and OpenCV via webcam.
# 🎯 Real-Time Object Detection with YOLOv8 & OpenCV

A lightweight real-time object detection app that uses your webcam and the YOLOv8 model to detect and label objects live on screen.

![Demo]()

---

## 📌 What It Does

- Captures live video from your webcam
- Runs **YOLOv8n** (nano — fast & lightweight) on every frame
- Draws bounding boxes and confidence scores around detected objects
- Press `q` to quit

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) | Object detection model |
| [OpenCV](https://opencv.org/) | Webcam capture & image display |
| Python 3.8+ | Language |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/yolo-webcam-detection.git
cd yolo-webcam-detection
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install ultralytics opencv-python
```

> **Note:** The YOLOv8n model weights (`yolov8n.pt`) will be **automatically downloaded** on first run. No manual download needed.

---

## ▶️ Run the Project

```bash
python detect.py
```

- A window titled **"YOLO Webcam"** will open showing live detections.
- Press **`q`** to exit.

---

## 📂 Project Structure

```
yolo-webcam-detection/
│
├── detect.py          # Main script
├── requirements.txt   # Dependencies
├── screenshot.png     # Demo screenshot
└── README.md          # This file
```

---

## 📋 requirements.txt

```
ultralytics
opencv-python
```

---

## 🧠 How It Works

1. **Model loads** — `YOLO("yolov8n.pt")` loads the pre-trained YOLOv8 nano model (trained on 80 COCO classes like person, bottle, phone, etc.)
2. **Webcam opens** — `cv2.VideoCapture(0)` accesses your default camera
3. **Frame loop** — Each frame is read and passed to the model
4. **Inference** — `model(frame)` runs detection and returns results
5. **Plotting** — `results[0].plot()` draws bounding boxes + labels + confidence scores
6. **Display** — `cv2.imshow()` renders the annotated frame in real time

---

## 🔍 Sample Output

In the demo screenshot, the model correctly detects:
- ✅ **Bottle** — 93% confidence (plastic water bottle)
- ⚠️ **Bird** — 27% confidence (butterfly pattern on wallpaper — a false positive!)

The low-confidence bird detection is a great example of how background patterns can sometimes confuse the model.

---

## 🚀 Possible Improvements

- [ ] Switch to `yolov8s.pt` or `yolov8m.pt` for better accuracy
- [ ] Add FPS counter on screen
- [ ] Filter detections by confidence threshold
- [ ] Save output video to file
- [ ] Count specific objects in frame

---

## 📄 License

MIT License — feel free to use and modify.

---

## 🙋 Author

**Your Name**  
[GitHub](https://github.com/YOUR_USERNAME) | [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
