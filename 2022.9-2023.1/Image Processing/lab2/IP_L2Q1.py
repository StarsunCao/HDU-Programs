import math
import cv2 as cv
import numpy as np

fn = "./image/yjsp.jpg"
""
# Read an image from file
img = cv.imread(fn, cv.IMREAD_COLOR)
if not isinstance(img, np.ndarray) or img.data is None:
    print("Error reading file \"{}\"".format(fn))
    exit()

#Conformal Transformations
#Shift
rows, cols = img.shape[0:2]
shift_x, shift_y = (50, 100)
T = np.float32([[1, 0, shift_x] , [0, 1, shift_y]])
img_shift = cv.warpAffine(img, T, (cols , rows))
cv.imshow("Shift", img_shift)

#Flip
rows, cols = img.shape[0:2]
#Flip around Ox
T = np.float32([[1,0,0],[0,-1,rows - 1]])
img_flip_y = cv.warpAffine(img, T, (cols,rows))
img_flip_y = cv.flip(img,0)
cv.imshow("Flip around Ox", img_flip_y)

#Flip around Oy
rows, cols = img.shape[0:2]
T = np.float32([[-1,0, cols - 1],[0, 1, 0]])
img_flip_x = cv.warpAffine(img, T, (cols,rows))
#img_flip_x = cv.flip(img,1)
cv.imshow("Flip around Oy", img_flip_x)

#Scaling
rows, cols = img.shape[0:2]
scale_x, scale_y = (0.5, 0.5)
T = np . float32 ([[ scale_x , 0 , 0] ,[0 , scale_y , 0]])
img_scale = cv.warpAffine (img, T,( int ( cols * scale_x ) ,int ( rows * scale_y )))
cv.imshow("Scale", img_scale)

# Rotation
rows, cols = img.shape[0:2]
phi = 17.0
phi_rad = phi * math.pi /180
# Take the top left corner as the origin of rotation
T = np.float32([[math.cos(phi_rad), -math.sin(phi_rad),0],
                [math.sin(phi_rad), math.cos(phi_rad),0]])
# Take the center as the origin of rotation
T1 = np.float32([[1, 0, -(cols - 1) / 2.0],[0, 1, -(rows - 1) / 2.0],[0, 0, 1]])
T2 = np.float32([[math.cos(phi_rad), -math.sin(phi_rad), 0],
                 [math.sin(phi_rad), math.cos(phi_rad), 0],[0, 0, 1]])
T3 = np.float32([[1, 0, (cols - 1) / 2.0],[0, 1, (rows - 1) / 2.0],[0, 0, 1]])
T = np.matmul(T3, np.matmul(T2, T1))[0:2, :]
# # Take the top left corner as the origin of rotation in a counterclockwise
# T = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), -phi, 1)
img_rotate = cv.warpAffine(img, T, (cols, rows))
cv.imshow("Rotate", img_rotate)


# Affine mapping
rows, cols = img.shape[0:2]
pts_src = np.float32([[50, 300], [150, 200], [50, 50]])
pts_dst = np.float32([[50, 200], [250, 200], [50, 100]])
T = cv.getAffineTransform(pts_src, pts_dst)
img_affine = cv.warpAffine(img, T, (cols, rows))

cv.polylines(img, [pts_src.astype(np.int32)],True, (0, 0, 0),1)
cv.polylines(img_affine, [pts_dst.astype(np.int32)], True, (0, 0, 0),1)
cv.imshow("Source", img)
cv.imshow("Affine", img_affine)

# Image Bevel
rows, cols = img.shape[0:2]
s = 0.3
T = np.float32([[1,s,0],[0,1,0]])
img_bevel = cv.warpAffine(img, T, (cols, rows))
cv.imshow("Bevel",img_bevel)

# Piecewise-Linear Mapping
stretch = 2
T = np . float32 ([[ stretch , 0, 0] , [0 , 1 , 0]])
rows, cols = img.shape[0:2]

img_left = img[:, 0:int(cols / 2), :]
img_right = img[:, int(cols/2):,:]
img_right = cv.warpAffine(img_right, T, (img_right.shape[1],rows))
img_plm = np.concatenate((img_left, img_right), axis = 1)

img_plm = img.copy()
img_plm[:, int(cols / 2):,:] = cv.warpAffine(img_plm[:, int(cols / 2):,:], T, (cols - int(cols / 2), rows))
cv.imshow("Piecewise-Linear", img_plm)

# Nonlinear Mappings
rows, cols = img.shape[0:2]
pts_src = np.float32([[50, 461], [461, 461], [461, 50], [50, 50]])
pts_dst = np.float32([[50, 461], [461, 440], [450, 10], [100, 50]])
T = cv.getPerspectiveTransform(pts_src, pts_dst)
#T = np.float32 ([[1.1 , 0.2, 0.00075] ,[0.35, 1.1 , 0.0005 ],[0, 0 , 1]])
img_persp = cv.warpPerspective (img , T ,(cols,rows))#int(cols * 1.5),int(rows * 1.5))

cv.polylines(img, [pts_src.astype(np.int32)], True, (0,0,0),1)
for i in range(4):
      src = np.float32([pts_src[i, 0], pts_src[i,1],1])
      pts_dst[i] = np.matmul(T[0:2,:],src)/np.matmul(T[2, :],src)
cv.polylines(img_persp, [pts_dst.astype(np.int32)], True, (0,0,0), 1)
cv.imshow("Projection", img_persp)

# Polynomial Mapping
rows, cols = img.shape[0:2]
T = np.array([[0,0],[1,0],[0,1],[0.00001,0],[0.002,0],[0.001,0]])
img_poly = np.zeros(img.shape, img.dtype)
if img.ndim ==2:
      for x in range(np.shape(img)[1]):
           for y in range(np.shape(img)[0]):
                 x_new = int(round(T[0,0] + x * T[1,0] + y * T[2,0] + x * x * T[3,0] + x * y * T[4,0] + y * y *T[5,0]))
                 y_new = int(round(T[0,1] + x * T[1,1] + y * T[2,1] + x * x * T[3,1] + x * y * T[4,1] + y * y *T[5,1]))
                 if x_new >= 0 and x_new < cols and y_new >=0 and y_new < rows:
                       img_poly[y_new, x_new] = img[y,x]
else:
      for x in range(np.shape(img)[1]):
           for y in range(np.shape(img)[0]):
                 x_new = int(round(T[0,0] + x * T[1,0] + y * T[2,0] + x * x * T[3,0] + x * y * T[4,0] + y * y *T[5,0]))
                 y_new = int(round(T[0,1] + x * T[1,1] + y * T[2,1] + x * x * T[3,1] + x * y * T[4,1] + y * y *T[5,1]))
                 if x_new >= 0 and x_new < cols and y_new >=0 and y_new < rows:
                       img_poly[y_new, x_new, :] = img[y,x,:]
cv.imshow("Polynomial", img_poly)

# Sinusoidal distortion
rows, cols = img.shape[0:2]
u , v = np . meshgrid ( np.arange ( cols ) ,np.arange ( rows ))
u = u + 20 * np . sin (2 * math . pi * v / 90)
img_sinusoid = cv.remap (img, u.astype ( np.float32 ) ,v.astype ( np.float32 ) , cv.INTER_LINEAR )
cv.imshow("Sinusoidal", img_sinusoid)

# Wait for a key press
cv.waitKey()
cv.destroyAllWindows()