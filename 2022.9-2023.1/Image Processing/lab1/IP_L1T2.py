import cv2
import numpy as np
import matplotlib.pyplot as plt


def projection_to_vertical(img):
    projection = np.zeros(img.shape[1])
    for i in range(img.shape[1]):
        projection[i] = np.sum(img[:, i])
    return projection


def projection_to_horizontal(img):
    projection = np.zeros(img.shape[0])
    for i in range(img.shape[0]):
        projection[i] = np.sum(img[i, :])
    return projection


def border(projection):
    p1 = 0
    p2 = 0
    for i in range(len(projection)):
        if projection[i] - projection[i + 1] > 500 and p1 == 0:
            p1 = i
            break

    for i in range(len(projection) - 1, 0, -1):
        if projection[i] - projection[i - 1] > 500 and p2 == 0:
            p2 = i
            break

    return p1, p2


img = cv2.imread('ys.png')
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
projection_to_horizontal = projection_to_horizontal(img)
projection_to_vertical = projection_to_vertical(img)
x1, x2 = border(projection_to_horizontal)
y1, y2 = border(projection_to_vertical)
xMax = projection_to_horizontal.max()
yMax = projection_to_vertical.max()
for i in range(len(projection_to_horizontal)):
    projection_to_horizontal[i] = -projection_to_horizontal[i] + xMax
for i in range(len(projection_to_vertical)):
    projection_to_vertical[i] = -projection_to_vertical[i] + yMax
plt.figure(1)
plt.plot(projection_to_horizontal)
plt.show()
plt.figure(2)
plt.plot(projection_to_vertical)
plt.show()
cv2.rectangle(img, (y1, x1), (y2, x2), (0, 255, 0), 4)
cv2.imshow('result', img)
cv2.waitKey(0)
