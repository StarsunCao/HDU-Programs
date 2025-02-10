import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_histogram(img):
    plt.figure(1)
    plt.plot(img)
    plt.savefig('3.jpg')
    plt.show()


def projection_to_vertical(img):
    projection = np.zeros(img.shape[1])
    for i in range(img.shape[1]):
        projection[i] = np.sum(img[:, i])
    return projection


img = cv2.imread('txm.jpg')
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
profile = img[round(img.shape[0] / 2), :]
profile = cv2.transpose(profile)
profile = cv2.flip(profile, 1)
projection = projection_to_vertical(profile)
show_histogram(projection)
cv2.imshow("profile", profile)
cv2.imwrite('profile.jpg', profile)
cv2.waitKey(0)
