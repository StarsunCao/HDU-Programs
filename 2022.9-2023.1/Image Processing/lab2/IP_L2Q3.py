import cv2 as cv
import numpy as np

# Manual
fn1 = "./image/yjsp_top.jpg"
fn2 = "./image/yjsp_bot.jpg"
# Read an images from files
img_top = cv.imread(fn1, cv.IMREAD_COLOR)
if not isinstance(img_top, np.ndarray) or img_top.data is None:
    print("Error reading file \" {}\"".format(fn1))
    exit()
img_bottom = cv.imread(fn2, cv.IMREAD_COLOR)
if not isinstance(img_bottom, np.ndarray) or img_bottom.data is None:
    print("Error reading file \" {}\"".format(fn2))
    exit()
cv.imshow("Top", img_top)
cv.imshow("Bottom", img_bottom)
# Match template
templ_size = 10
templ = img_top[- templ_size:, :, :]
res = cv.matchTemplate(img_bottom, templ,
                       cv.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# Stitch images
img_stitch = np.zeros((img_top.shape[0] + img_bottom.shape[0] - max_loc[1] - templ_size, img_top.shape[1],
                       img_top.shape[2]), dtype=np.uint8)
img_stitch[0: img_top.shape[0], :, :] = img_top
img_stitch[img_top.shape[0]:, :, :] = img_bottom[max_loc[1] + templ_size:, :, :]
cv.imshow("Stitch", img_stitch)


# Wait for a key press
cv.waitKey()
cv.destroyAllWindows()