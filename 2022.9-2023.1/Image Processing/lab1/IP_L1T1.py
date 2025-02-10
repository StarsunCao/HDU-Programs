import cv2
import numpy as np
from matplotlib import pyplot as plt


def grey_scale(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    input_min, input_max = img_gray.min(), img_gray.max()
    print('input_min = %d,input_max = %d' % (input_min, input_max))
    output = np.uint8(255 / (input_max - input_min) * (img_gray - input_min) + 0.5)
    return output


def show_histogram(fx, gx):
    plt.figure(1)
    plt.hist(fx.ravel(), 256, [0, 256])
    plt.figure(2)
    plt.hist(gx.ravel(), 256, [0, 256])
    plt.show()


img = cv2.imread('yjsp.jpg')
greyScale = grey_scale(img)
cv2.imshow('img', img)
cv2.imshow('imgGray', cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.imshow('greyScale', greyScale)
show_histogram(img, greyScale)
cv2.waitKey(0)