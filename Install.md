# Install OpenCV

Before install OpenCV on your computer, please check you version of system.
In my case, I use Debain with WSL enviroments.
In same case with me, We can easily check out our version with next few steps.

Open your kernel, then type this
`cat /etc/os-release`
And the output displayed like this,
`
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
`
After that follow the documents written by OpenCV[1] by your OS envirments.

In my case, I use conda envirments, And also i want to add a new env for OpenCV.

`
conda create 'opencv'
conda activate opencv
pip install opencv-python
`

After download opencv successfully
double checked with called version of opencv

I was used ipython if you want use ipython please install jupyter in your env.
`
import cv2 as cv # cv2 is library name of openCV
print(cv.__version__)
`

then you can check your openCV version on kernel, I got the result.
`4.10.0`

You can also findout this information on OpenCV official tutorial documents[1]

---
[1] https://docs.opencv.org/4.x/d0/d3d/tutorial_general_install.htmlcat
