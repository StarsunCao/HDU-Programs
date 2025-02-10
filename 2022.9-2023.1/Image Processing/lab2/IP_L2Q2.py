import cv2 as cv
import numpy as np

fn = "./image/yjsp.jpg"

# Read an image from file
img = cv.imread(fn, cv.IMREAD_COLOR)
if not isinstance(img, np.ndarray) or img.data is None:
    print("Error reading file \"{}\"".format(fn))
    exit()

cv.imshow("Source", img)

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

u, v = cv.polarToCart(r, theta)
u = u * xmid + xmid
v = v * ymid + ymid
img_corr = cv.remap(img_barrel, u.astype(np.float32), v.astype(np.float32), cv.INTER_LINEAR)
cv.imshow("Corrected", img_corr)

# Wait for a key press
cv.waitKey()
cv.destroyAllWindows()