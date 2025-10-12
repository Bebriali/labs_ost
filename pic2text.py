import cv2
import easyocr

reader = easyocr.Reader(['ru', 'en'])  # Поддержка русского и английского
cap = cv2.VideoCapture("video.mp4")
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % fps == 0:
        results = reader.readtext(frame, detail=0)
        print(f"Время {frame_count // fps} сек: {' '.join(results)}")
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
