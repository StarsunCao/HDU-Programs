import cv2
import numpy as np




# 读取原始图像和经过差分算子处理后的图像
img1 = cv2.imread('2.png')

# 将图像转为灰度图
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


# 应用Canny边缘检测
edges1 = cv2.Canny(gray1, 50, 150, apertureSize=3)

# 应用霍夫变换查找圆
circles1 = cv2.HoughCircles(edges1, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# 在原始图像上绘制圆
if circles1 is not None:
    circles1 = np.round(circles1[0, :]).astype("int")
    for (x, y, r) in circles1:
        cv2.circle(img1, (x, y), r, (0, 255, 0), 2)

# 显示结果
cv2.imshow('Image 1 with Circles', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()