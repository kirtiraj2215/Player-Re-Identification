from deep_sort_realtime.deepsort_tracker import DeepSort

class PlayerTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=60)

    def update(self, frame, boxes):
        detections = [(box, 1.0, 'player') for box in boxes]
        tracks = self.tracker.update_tracks(detections, frame=frame)
        results = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()
            results.append((track_id, ltrb))
        return results