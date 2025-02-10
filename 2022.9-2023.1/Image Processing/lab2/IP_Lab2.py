# #导入cv模块
# import cv2 as cv
# #读取图像，支持 bmp、jpg、png、tiff 等常用格式
# img = cv.imread("./test.jpg")
# #创建窗口并显示图像
# cv.namedWindow("Image")
# cv.imshow("Image",img)
# cv.waitKey(0)
# #释放窗口
# cv.destroyAllWindows()
import math
import cv2 as cv
import numpy as np


# Draw a plot in a given image drawing context
# @param[in, out] image image drawing context
# @param[in] data_array data to draw
# @param[in] color color to use when drawing
# @param[in] max_val scale factor for the histogram values (default is 1)
def DrawGraph(image, data_array, color, max_val=1.0):
    image_w = image.shape[1]
    image_h = image.shape[0]
    data_size = data_array.shape[0]

    step = image_w / data_size
    x = step * 0.5
    cv.line(image,
            (0, image_h - 1 - int((image_h - 1) * data_array[0] / max_val)),
            (int(x), image_h - 1 - int((image_h - 1) * data_array[0] / max_val)),
            color, thickness=1)

    for i in range(1, data_size):
        cv.line(image,
                (int(x), image_h - 1 - int((image_h - 1) * data_array[i - 1] / max_val)),
                (int(x + step), image_h - 1 - int((image_h - 1) * data_array[i] / max_val)),
                color, thickness=1)
        x += step

    cv.line(image,
            (int(x), image_h - 1 - int((image_h - 1) * data_array[data_size - 1] / max_val)),
            (image_w - 1, image_h - 1 - int((image_h - 1) * data_array[data_size - 1] / max_val)),
            color, thickness=1)


# Draw a histogram in a given image drawing context
# @param[in, out] image image drawing context
# @param[in] data_array data to draw
# @param[in] color color to use when drawing
# @param[in] max_val scale factor for the histogram values (default is 1)
def DrawHist(image, data_array, color, max_val=1.0):
    image_w = image.shape[1]
    image_h = image.shape[0]
    data_size = data_array.shape[0]

    step = image_w / data_size
    x = 0
    for i in range(0, data_size):
        cv.rectangle(image,
                     (int(x), image_h - 1 - int((image_h - 1) * data_array[i] / max_val)),
                     (int(x + step) - 1, image_h - 1),
                     color, thickness=-1)
        x += step


# Export a matrix into a file
# @param[out] fn file name
# @param[in] mat matrix to export
# @param[in] delimiter delimiter between columns
def ExportText(fn, mat, delimiter='\t'):
    if mat.ndim > 2:
        mat_out = mat.reshape(mat.shape[0], -1)
    else:
        mat_out = mat
    if mat.dtype == np.uint8:
        format = "%i"
    else:
        format = "%f"
    np.savetxt(fn, mat_out, fmt=format, delimiter=delimiter)


#
# Main function
#

fn = "./image/yjsp.jpg"

# Read an image from file
img = cv.imread(fn, cv.IMREAD_COLOR)
if not isinstance(img, np.ndarray) or img.data is None:
    print("Error reading file \"{}\"".format(fn))
    exit()

# Convert loaded image to gray scale
img_bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Save gray scale image
cv.imwrite("./image/meinv_bw.jpg", img_bw)

# # Show both images
# cv.imshow("Color", img)
# cv.imshow("BW", img_bw)


cv.imshow("Source", img)
# #Conformal Transformations
# #Shift
# rows, cols = img.shape[0:2]
# shift_x, shift_y =(50, 100)
# T = np.float32([[1, 0, shift_x],[0, 1, shift_y]])
# img_shift = cv.warpAffine(img, T, (cols,rows))
# cv.imshow("Shift", img_shift)

# #Flip
# rows, cols = img.shape[0:2]
# #Flip around Ox
# T = np.float32([[1,0,0],[0,-1,rows - 1]])
# img_flip_y = cv.warpAffine(img, T, (cols,rows))
# #img_flip_y = cv.flip(img,0)
# cv.imshow("Flip around Ox", img_flip_y)

# #Flip around Oy
# rows, cols = img.shape[0:2]
# T = np.float32([[-1,0, cols - 1],[0, 1, 0]])
# img_flip_x = cv.warpAffine(img, T, (cols,rows))
# #img_flip_x = cv.flip(img,1)
# cv.imshow("Flip around Oy", img_flip_x)

# #Scaling
# rows, cols = img.shape[0:2]
# scale_x, scale_y = (0.5, 0.5)
# T = np . float32 ([[ scale_x , 0 , 0] ,[0 , scale_y , 0]])
# img_scale = cv.warpAffine (img, T,( int ( cols * scale_x ) ,int ( rows * scale_y )))
# cv.imshow("Scale", img_scale)

# # Rotation
# rows, cols = img.shape[0:2]
# phi = 17.0
# phi_rad = phi * math.pi /180
# # Take the top left corner as the origin of rotation
# T = np.float32([[math.cos(phi_rad), -math.sin(phi_rad),0],
#                 [math.sin(phi_rad), math.cos(phi_rad),0]])
# # Take the center as the origin of rotation
# T1 = np.float32([[1, 0, -(cols - 1) / 2.0],[0, 1, -(rows - 1) / 2.0],[0, 0, 1]])
# T2 = np.float32([[math.cos(phi_rad), -math.sin(phi_rad), 0],
#                  [math.sin(phi_rad), math.cos(phi_rad), 0],[0, 0, 1]])
# T3 = np.float32([[1, 0, (cols - 1) / 2.0],[0, 1, (rows - 1) / 2.0],[0, 0, 1]])
# T = np.matmul(T3, np.matmul(T2, T1))[0:2, :]
# # # Take the top left corner as the origin of rotation in a counterclockwise
# # T = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), -phi, 1)
# img_rotate = cv.warpAffine(img, T, (cols, rows))
# cv.imshow("Rotate", img_rotate)

# # Affine mapping
# rows, cols = img.shape[0:2]
# pts_src = np.float32([[50, 300], [150, 200], [50, 50]])
# pts_dst = np.float32([[50, 200], [250, 200], [50, 100]])
# T = cv.getAffineTransform(pts_src, pts_dst)
# img_affine = cv.warpAffine(img, T, (cols, rows))

# cv.polylines(img, [pts_src.astype(np.int32)],True, (0, 0, 0),1)
# cv.polylines(img_affine, [pts_dst.astype(np.int32)], True, (0, 0, 0),1)
# cv.imshow("Source", img)
# cv.imshow("Affine", img_affine)

# # Image Bevel
# rows, cols = img.shape[0:2]
# s = 0.3
# T = np.float32([[1,s,0],[0,1,0]])
# img_bevel = cv.warpAffine(img, T, (cols, rows))
# cv.imshow("Bevel",img_bevel)

# # Piecewise-Linear Mapping
# stretch = 2
# T = np . float32 ([[ stretch , 0, 0] , [0 , 1 , 0]])
# rows, cols = img.shape[0:2]

# img_left = img[:, 0:int(cols / 2), :]
# img_right = img[:, int(cols/2):,:]
# img_right = cv.warpAffine(img_right, T, (img_right.shape[1],rows))
# img_plm = np.concatenate((img_left, img_right), axis = 1)

# img_plm = img.copy()
# img_plm[:, int(cols / 2):,:] = cv.warpAffine(img_plm[:, int(cols / 2):,:], T, (cols - int(cols / 2), rows))
# cv.imshow("Piecewise-Linear", img_plm)

# # Nonlinear Mappings
# rows, cols = img.shape[0:2]
# pts_src = np.float32([[50, 461], [461, 461], [461, 50], [50, 50]])
# pts_dst = np.float32([[50, 461], [461, 440], [450, 10], [100, 50]])
# T = cv.getPerspectiveTransform(pts_src, pts_dst)
# #T = np.float32 ([[1.1 , 0.2, 0.00075] ,[0.35, 1.1 , 0.0005 ],[0, 0 , 1]])
# img_persp = cv.warpPerspective (img , T ,(cols,rows))#int(cols * 1.5),int(rows * 1.5))

# cv.polylines(img, [pts_src.astype(np.int32)], True, (0,0,0),1)
# for i in range(4):
#       src = np.float32([pts_src[i, 0], pts_src[i,1],1])
#       pts_dst[i] = np.matmul(T[0:2,:],src)/np.matmul(T[2, :],src)
# cv.polylines(img_persp, [pts_dst.astype(np.int32)], True, (0,0,0), 1)
# cv.imshow("Projection", img_persp)

# # Polynomial Mapping
# rows, cols = img.shape[0:2]
# T = np.array([[0,0],[1,0],[0,1],[0.00001,0],[0.002,0],[0.001,0]])
# img_poly = np.zeros(img.shape, img.dtype)
# if img.ndim ==2:
#       for x in range(np.shape(img)[1]):
#            for y in range(np.shape(img)[0]):
#                  x_new = int(round(T[0,0] + x * T[1,0] + y * T[2,0] + x * x * T[3,0] + x * y * T[4,0] + y * y *T[5,0]))
#                  y_new = int(round(T[0,1] + x * T[1,1] + y * T[2,1] + x * x * T[3,1] + x * y * T[4,1] + y * y *T[5,1]))
#                  if x_new >= 0 and x_new < cols and y_new >=0 and y_new < rows:
#                        img_poly[y_new, x_new] = img[y,x]
# else:
#       for x in range(np.shape(img)[1]):
#            for y in range(np.shape(img)[0]):
#                  x_new = int(round(T[0,0] + x * T[1,0] + y * T[2,0] + x * x * T[3,0] + x * y * T[4,0] + y * y *T[5,0]))
#                  y_new = int(round(T[0,1] + x * T[1,1] + y * T[2,1] + x * x * T[3,1] + x * y * T[4,1] + y * y *T[5,1]))
#                  if x_new >= 0 and x_new < cols and y_new >=0 and y_new < rows:
#                        img_poly[y_new, x_new, :] = img[y,x,:]
# cv.imshow("Polynomial", img_poly)

# # Sinusoidal distortion
# rows, cols = img.shape[0:2]
# u , v = np . meshgrid ( np.arange ( cols ) ,np.arange ( rows ))
# u = u + 20 * np . sin (2 * math . pi * v / 90)
# img_sinusoid = cv.remap (img, u.astype ( np.float32 ) ,v.astype ( np.float32 ) , cv.INTER_LINEAR )
# cv.imshow("Sinusoidal", img_sinusoid)

# # Barrel distortion
# Create mesh grid for X , Y
rows, cols = img.shape[0:2]
xi, yi = np.meshgrid(np.arange(cols), np.arange(rows))
# Shift and normalize grid
xmid = cols / 2.0
ymid = rows / 2.0
xi = xi - xmid
yi = yi - ymid
# Convert to polar and do transformation
r, theta = cv.cartToPolar(xi / xmid, yi / ymid)
# F3 = 0.1
# F5 = 0.12
# r = r + F3 * r ** 3 + F5 * r ** 5
F1 = 0.99992415
F2 = -0.00351985
F3 = -0.05908754
F4 = -0.13945222
F5 = 0.0745766
r = F1 * r + F2 * r ** 2 + F3 * r ** 3 + F4 * r ** 4 + F5 * r ** 5
# Undo conversion , normalization and shift
u, v = cv.polarToCart(r, theta)
u = u * xmid + xmid
v = v * ymid + ymid
# Do remapping
img_barrel = cv.remap(img, u.astype(np.float32), v.astype(np.float32), cv.INTER_LINEAR)
cv.imshow("Distorted", img_barrel)

# # Correction
d = 5
max_r = 1.3
pts = (np.arange(d, dtype=np.float32) + 1) / d * max_r
# #Barrel
# pts2 = pts + F3 * pts ** 3 + F5 + pts ** 5
# Pincushion
pts2 = F1 * pts + F2 * pts ** 2 + F3 * pts ** 3 + F4 * pts ** 4 + F5 * pts ** 5

# create and fill matrix
T = np.zeros((d, d))
for i in range(d):
    T[:, i] = pts2 ** (i + 1)
T = np.linalg.inv(T)
F = np.matmul(T, pts)

r, theta = cv.cartToPolar(xi / xmid, yi / ymid)
rt = 0
for i in range(d):
    rt = rt + F[i] * r ** (i + 1)
r = rt

# F1 = 0.99992415
# F2 =-0.00351985
# F3 =-0.05908754
# F4 =-0.13945222
# F5 = 0.0745766
# r = F1 * r + F2 * r ** 2 + F3 * r ** 3+F4 * r ** 4 + F5 * r ** 5 + F6 * r ** 6

u, v = cv.polarToCart(r, theta)
u = u * xmid + xmid
v = v * ymid + ymid
img_corr = cv.remap(img_barrel, u.astype(np.float32), v.astype(np.float32), cv.INTER_LINEAR)
cv.imshow("Corrected", img_corr)

# Manual
# fn1 = "./image/meinvTop.jpg"
# fn2 = "./image/meinvBot.jpg"
# # Read an images from files
# img_top = cv.imread(fn1, cv.IMREAD_COLOR)
# if not isinstance(img_top, np.ndarray) or img_top.data is None:
#     print("Error reading file \" {}\"".format(fn1))
#     exit()
# img_bottom = cv.imread(fn2, cv.IMREAD_COLOR)
# if not isinstance(img_bottom, np.ndarray) or img_bottom.data is None:
#     print("Error reading file \" {}\"".format(fn2))
#     exit()
# cv.imshow("Top", img_top)
# cv.imshow("Bottom", img_bottom)
# # Match template
# templ_size = 10
# templ = img_top[- templ_size:, :, :]
# res = cv.matchTemplate(img_bottom, templ,
#                        cv.TM_CCOEFF)
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# # Stitch images
# img_stitch = np.zeros((img_top.shape[0] + img_bottom.shape[0] - max_loc[1] - templ_size, img_top.shape[1],
#                        img_top.shape[2]), dtype=np.uint8)
# img_stitch[0: img_top.shape[0], :, :] = img_top
# img_stitch[img_top.shape[0]:, :, :] = img_bottom[max_loc[1] + templ_size:, :, :]
# cv.imshow("Stitch", img_stitch)


# Wait for a key press
cv.waitKey()
cv.destroyAllWindows()