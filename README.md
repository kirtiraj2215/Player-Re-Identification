# Player Re-Identification 

## 🎯 Task
Identify players in a single video and ensure consistent ID assignment even if they leave and re-enter the frame.

## 📁 Folder Structure
```
player-reid/
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── detector.py         # YOLOv11 detection logic
│   ├── tracker.py          # Deep SORT tracking implementation
│   ├── utils.py            # Helper functions
│   └── visualizer.py       # Annotation and rendering
├── models/                 # YOLOv11 fine-tuned model file
│   └── yolov11_player.pt
├── data/                   # Input video
│   └── input_video.mp4
├── output/                 # Result video and annotations
│   ├── output_video.mp4
│   └── tracking_results.json
├── requirements.txt        # Python dependencies
├── run.py                  # Main execution script
├── README.md              # This file
└── report.md              # Detailed project report
```

## 🚀 Setup

### Prerequisites
- Python 3.10+
- CUDA-compatible GPU (recommended)
- FFmpeg for video processing

### Installation
```bash
# Create conda environment
conda create -n player_reid python=3.10 -y
conda activate player_reid

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
```txt
ultralytics>=8.0.0
opencv-python>=4.8.0
torch>=2.0.0
torchvision>=0.15.0
numpy>=1.24.0
deep-sort-realtime>=1.3.2
scipy>=1.10.0
matplotlib>=3.7.0
```

## 🎮 Usage

### Basic Run
```bash
python run.py
```
