# Zupix 🖐️

Zupix is a Python based virtual zoom system that uses hand gestures to zoom in and out on an image in real time. Show your thumb and index fingers from both hands, and it will respond by zooming the image accordingly.

![Zupix Demo](demo.gif)  

## ✨ Features

| Feature                   | Description                              |
|---------------------------|------------------------------------------|
| 📷 Hand Detection         | Tracks both hands in real time           |
| 🤏 Gesture Zoom           | Pinch gesture to zoom in/out             |
| 🖼️ Image Zoom             | Zooms image based on finger distance     |
| 🖥️ Interactive UI         | Simple and clean user interface          |
| 🔁 Live Zoom Tracking     | Continuously updates zoom level          |
| ⚡ Fast & Lightweight     | Optimized for real-time use              |
| 🧩 Customizable           | Easy to modify and extend                |

---

## 🛠️ Tech Stack

- Python 🐍  
- OpenCV 📷  
- Mediapipe 🖐️  

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Zupix.git
cd Zupix
````

### 2. Install dependencies

Make sure you have Python 3.7+ installed. Then install required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python zupix.py
```

## 🧠 How It Works

Zupix uses **Mediapipe** to detect hand landmarks. When the index finger and thumb tips of both hands are detected, the script calculates the distance between them to determine zoom level. The image scales accordingly, mimicking a real pinch zoom gesture.

