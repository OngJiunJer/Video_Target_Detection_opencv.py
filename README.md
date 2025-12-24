# Video_Target_Detection_opencv.py
This Python project detects a specific target image in a video using OpenCV’s template matching. It identifies all frames where the target appears, records the frame number, timestamp, position, size, and matching confidence, and optionally saves annotated frames. The results are exported to a CSV file for easy analysis.

# Features
- Detect a target image in a video frame by frame
- Save detection information including:
  - Frame number
  - Time in seconds
  - X, Y coordinates
  - Width and height of the detected target
  - Matching confidence score
- Highlight detected targets with rectangles on frames and save them as images
- Export all detection data to a CSV file

# Requirements
- Python 3.x
- OpenCV (opencv-python)
- CSV (built-in Python library)

# Code Explanation
- min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  - min_val  -> minimum matching score in the matrix (worst match)
  - max_val  -> maximum matching score in the matrix (best match)
  - min_loc  -> coordinates of minimum value
  - max_loc  -> coordinates of maximum value
 
- results.append([frame_index, time_in_seconds, x, y, w, h, float(max_val)])
- results.append([frame, fps, x-axis, y-axis, width, height, maximum number of validation])
  - frame_index → the frame number in the video
  - time_in_seconds → the timestamp of that frame in seconds
  - x → X-coordinate of the top-left corner of the detected target
  - y → Y-coordinate of the top-left corner of the detected target
  - w → width of the target (from template image)
  - h → height of the target (from template image)
  - float(max_val) → the confidence score of the template match (how similar the detected region is to the target)
 
 # Data: Tom and Jerry MP4 Video & Target.jpg
 - This video is gained from a Kaggle platform Link: https://www.kaggle.com/datasets/ziya07/detect-emotions-of-your-favorite-toons
 - And all the Target.jpg data is a screenshot from the Tom and Jerry MP4 Video.

 
