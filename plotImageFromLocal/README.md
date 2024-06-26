# Introduction
On this project, We test that plot the local image file on our screen with OpenCV.

# Goal
Showing selected our local image with openCV

# Warining
It is seem to easy but if you don't have any information about any video output mechanism on Linux, it might be much harder then you thought.

# Explanation
Follow the openCV documents about this test [1]

We can easily plot,
```
    import cv2 as cv
    import sys

    img = cv.imread(cv.samples.findFile('shota_Imanaga.jpg'))
    cv.imshow("Display window" img)
    k = cv.waitKey(0) 
```
##If you can not select your image you can follow my preference.

*Encountered Issue
```
In [5]: cv.imshow("Display window", img)
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/uni/anaconda3/envs/opencv/lib/python3.12/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, eglfs, minimal, minimalegl, offscreen, vnc, webgl.
```
This issue arises from Windows and Linux display the image to our monitors with diffrent systems.
Linux traditionaly use X11 protocol supported by X.org Server.
Windows use DiretX Libarary.
So if you want to work in wsl not using other Virtual Machine for Linux enviroments, may be need to support external program for displaying with X11 protocol.<br>

* Solution
In my case i chose Xming.
I install the Xming system follow by this documents[2].

* Caution
If you using ipython, You must be put `cv.waitkey()` after `cv.imshow()`, after put `cv.waitKey()` the image plot on Xming windows.

---
ref 
[1] https://docs.opencv.org/4.x/db/deb/tutorial_display_image.html
[2] https://www.uwyo.edu/data-science/resources/knowledge-base/x11-with-windows-subsystem-for-linux.html