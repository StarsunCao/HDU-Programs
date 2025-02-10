import cv2
import matplotlib.pyplot as plt
import numpy as np


o = cv2.imread('Queen Elizabeth.png')

"""Roberts算子"""
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
x = cv2.filter2D(o, cv2.CV_16S, kernelx)
y = cv2.filter2D(o, cv2.CV_16S, kernely)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

fig1, axes = plt.subplots(1,2, figsize=(10,5), dpi=100)
axes[0].imshow(o[:,:,::-1])
axes[1].imshow(Roberts[:,:,::-1])
plt.savefig('High-pass filtering/Roberts Filter.png', dpi=600,bbox_inches='tight')


"""Prewitt算子"""
kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv2.filter2D(o, cv2.CV_16S, kernelX)
y = cv2.filter2D(o, cv2.CV_16S, kernelY)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

fig2, axes = plt.subplots(1,2, figsize=(10,5), dpi=100)
axes[0].imshow(o[:,:,::-1])
axes[1].imshow(Prewitt[:,:,::-1])
plt.savefig('High-pass filtering/Prewitt Filter.png', dpi=600,bbox_inches='tight')

"""Sobel算子"""
Sobelx = cv2.Sobel(o, cv2.CV_64F,1,0)
Sobely = cv2.Sobel(o, cv2.CV_64F,0,1)
Sobelx = cv2.convertScaleAbs(Sobelx)
Sobely = cv2.convertScaleAbs(Sobely)
Sobelxy = cv2.addWeighted(Sobelx,0.5, Sobely,0.5,0)
Sobelxy11 = cv2.Sobel(o, cv2.CV_64F,1,1)
Sobelxy11 = cv2.convertScaleAbs(Sobelxy11)


fig3, axes = plt.subplots(1,3, figsize=(10,5), dpi=100)
axes[0].imshow(o[:,:,::-1])
axes[1].imshow(Sobelxy[:,:,::-1])
axes[2].imshow(Sobelxy11[:,:,::-1])
plt.savefig('High-pass filtering/Sobel Filter.png', dpi=600,bbox_inches='tight')

"""Laplacian算子"""
Laplacian = cv2.Laplacian(o, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)
fig4, axes = plt.subplots(1,2, figsize=(10,5), dpi=100)
axes[0].imshow(o[:,:,::-1])
axes[1].imshow(Laplacian[:,:,::-1])
plt.savefig('High-pass filtering/Laplace Filter.png', dpi=600,bbox_inches='tight')

"""Canny边缘检测"""

r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)
o_grey=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
fig5, axes = plt.subplots(1,3, figsize=(10,5), dpi=100)
imgs=np.hstack([o_grey,r1,r2])
cv2.imshow("Canny Algorithm",imgs)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('High-pass filtering/Canny Algorithm.png', imgs)



