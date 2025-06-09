from ultralytics import YOLO
import cv2

class PlayerDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_players(self, frame):
        results = self.model.predict(frame, conf=0.4, iou=0.5)
        players = []
        for r in results:
            for box, cls in zip(r.boxes.xyxy, r.boxes.cls):
                if int(cls) == 0: 
                    x1, y1, x2, y2 = map(int, box.tolist())
                    players.append([x1, y1, x2, y2])
        return players