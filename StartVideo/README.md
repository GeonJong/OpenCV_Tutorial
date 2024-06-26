# Introduction
In this session, I explain how we playing video from file followed by OpenCV documents [1].

# Goal
Play local videos with OpenCV

# Explaination

Follow the documents, you can see your videos playing on Xming well.

```
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('ImanagaShota.mp4')

while cap.isOpened():
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
```

---
ref<br>
[1] https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html <br>