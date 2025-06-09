# 🏃 Player Re-Identification – Liat.ai Assignment (Option 2)

This repository contains a complete pipeline for **real-time player re-identification** in a single 15-second sports video. It ensures consistent player IDs even when players leave and re-enter the frame using object detection and tracking.

## 📁 Project Structure
```
player-reid-liat/
├── models/                     # Pre-trained YOLOv11 model
│   └── yolov11_player.pt
├── data/                       # Input videos
│   └── 15sec_input_720p.mp4
├── output/                     # Output video
│   └── result.mp4
├── src/                        # Core modules
│   ├── detector.py             # YOLOv11 detection wrapper
│   ├── tracker.py              # DeepSORT tracking
│   └── utils.py                # Drawing utilities
├── run.py                      # Main execution script
├── create_env.sh              # Conda environment setup
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── report.md                   # Approach and methodology
```
---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/player-reid-liat.git
cd player-reid-liat
