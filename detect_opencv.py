# Install OpenCV
#exit()
#pip install opencv-python

import cv2
import csv

# Input files
video_path = "sample.mp4"
template_path = "tag_template_v2.png"

# Load template
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

# Open video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

frame_index = 0
results = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Template matching
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If score is high → tag detected
    if max_val > 0.75:  
        x, y = max_loc
        time_in_seconds = frame_index / fps

        results.append([frame_index, time_in_seconds, x, y, w, h, float(max_val)])

        # Optional: save annotated frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
        cv2.imwrite(f"frame_{frame_index}.jpg", frame)

    frame_index += 1

cap.release()

# Save output CSV
with open("detections.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["frame", "time_s", "x", "y", "w", "h", "score"])
    writer.writerows(results)

print("Done. Frames detected:", len(results))
