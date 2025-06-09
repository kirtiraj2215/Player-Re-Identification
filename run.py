import cv2
from src.detector import PlayerDetector
from src.tracker import PlayerTracker
from src.utils import draw_boxes

video_path = '/Users/kirtirajjamnotiya/Desktop/Summer_2025/Liat.ai Assignment/data/15sec_input_720p.mp4'
model_path = '/Users/kirtirajjamnotiya/Desktop/Summer_2025/Liat.ai Assignment/models/best.pt'
output_path = 'output/result.mp4'

detector = PlayerDetector(model_path)
tracker = PlayerTracker()

cap = cv2.VideoCapture(video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    boxes = detector.detect_players(frame)
    tracked = tracker.update(frame, boxes)
    frame = draw_boxes(frame, tracked)
    out.write(frame)
    cv2.imshow('Re-ID Output', frame)
    if cv2.waitKey(1) == 27: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()