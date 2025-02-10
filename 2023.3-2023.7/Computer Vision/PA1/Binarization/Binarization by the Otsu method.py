# This code reads an image and applies the Otsu method for binarization
# Importing the necessary libraries
import cv2

# Reading the image in grayscale
I = cv2.imread("yjsp.jpg", cv2.IMREAD_GRAYSCALE)

# Applying the Otsu method for binarization
ret, Inew = cv2.threshold(I, 0, 255,
                          cv2.THRESH_OTSU)

# Displaying the binarized image
cv2.imshow( "Binarization by the Otsu method" , Inew)
cv2.waitKey(0)
