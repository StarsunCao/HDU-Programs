# Importing necessary libraries
import numpy as np
import cv2

# Defining function for skin color segmentation
def SkinColorSegmentation(imname):
  # Reading image
  img = cv2.imread(imname, cv2.IMREAD_COLOR)
  # Converting image to HSV color space
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  (_h, _s, _v) = cv2.split(hsv)
  # Creating an array of zeros with the same shape as _h
  skin3 = np.zeros(_h.shape, dtype=np.uint8)
  (x, y) = _h.shape
  # Looping through each pixel of the image
  for i in range(0, x):
    for j in range(0, y):
      # Checking if the pixel is within the skin color range
      if (_h[i][j] > 7) and (_h[i][j] < 20) and (_s[i][j] > 28) and (_s[i][j] < 255) and (_v[i][j] > 50) and (
        _v[i][j] < 255):
        # Setting the pixel value to 255 if it is within the skin color range
        skin3[i][j] = 255
      else:
        # Setting the pixel value to 0 if it is not within the skin color range
        skin3[i][j] = 0
        
  # Displaying the original image and the skin color segmented image
  cv2.imshow(imname, img)
  cv2.imshow(imname + " Skin3 HSV", skin3)

# Running the function on the given image
if __name__=="__main__":
  imname="van.jpg"
  SkinColorSegmentation(imname)
  cv2.waitKey(0)


