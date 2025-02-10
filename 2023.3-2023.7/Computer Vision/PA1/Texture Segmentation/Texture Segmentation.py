import cv2
import numpy as np
from skimage import filters, morphology
from PA1_Appendix import bwareaopen, imfillholes

# Read the image in grayscale
I = cv2.imread("jzdc.jpg",cv2.IMREAD_GRAYSCALE)

# Calculate the entropy of the image
E = filters.rank.entropy(I,morphology.square(9)).astype(np.float32)

# Normalize the entropy image
Eim = (E - E.min()) / (E.max() - E.min())

# Display the entropy image
cv2.imshow("E", Eim)

# Threshold the entropy image using Otsu's method
ret, BW1 = cv2.threshold(np.uint8(Eim * 255), 0, 255,cv2.THRESH_OTSU)

# Display the thresholded image
cv2.imshow("BW1", BW1)

# Remove small objects from the thresholded image
BWao = bwareaopen(BW1, 2000)

# Define a structuring element for morphological operations
nhood = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

# Close the thresholded image
closeBWao = cv2.morphologyEx(BWao, cv2.MORPH_CLOSE, nhood)

# Fill holes in the closed image
Mask1 = imfillholes(closeBWao)

# Display the processed images
cv2.imshow("After bwareaopen 1", BWao)
cv2.imshow("After close 1", closeBWao)
cv2.imshow("After fill holes 1", Mask1)

# Find contours in the filled image
contours, h = cv2.findContours(Mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Create a binary image of the contour boundary
boundary = np.zeros_like(Mask1)
cv2.drawContours(boundary, contours, -1, 255, 1)

# Create a segmented image using the boundary
segmentResults = I.copy()
segmentResults[boundary != 0] = 255

# Display the segmented image
cv2.imshow("Segment result 1", segmentResults)

# Create a masked image of the original image
I2 = I . copy ()
I2 [ Mask1 != 0] = 0

# Calculate the entropy of the masked image
E2 = filters . rank . entropy ( I2 , morphology . square (9)). astype ( np . float32 )

# Normalize the entropy image
Eim2 = ( E2 - E2 . min ()) / ( E2 . max () - E2 . min ())

# Display the entropy image
cv2.imshow("E2", Eim2)

# Threshold the entropy image using Otsu's method
ret , BW2 = cv2 . threshold ( np . uint8 ( Eim2 * 255) , 0 , 255 , cv2 . THRESH_OTSU )

# Display the thresholded image
cv2.imshow("BW2", BW2)

# Remove small objects from the thresholded image
BW2ao = bwareaopen ( BW2 , 2000)

# Close the thresholded image
closeBW2ao = cv2 . morphologyEx ( BW2ao , cv2 . MORPH_CLOSE , nhood )

# Fill holes in the closed image
Mask2 = imfillholes ( closeBW2ao )

# Display the processed images
cv2.imshow("After bwareaopen 2", BWao)
cv2.imshow("After close 2", closeBWao)
cv2.imshow("After fill holes 2", Mask1)

# Find contours in the filled image
contours2 , h = cv2 . findContours ( Mask2 , cv2 . RETR_TREE , cv2 . CHAIN_APPROX_NONE )

# Create a binary image of the contour boundary
boundary2 = np . zeros_like ( Mask2 )
cv2 . drawContours ( boundary2 , contours2 , -1 , 255 , 1)

# Create a segmented image using the boundary
segmentResults2 = I2 . copy ()
segmentResults2 [ boundary2 != 0] = 255

# Display the segmented image
cv2.imshow("Segment result 2", segmentResults2)

# Create a masked image of the original image
texture1 = I . copy ()
texture1 [ Mask2 == 0] = 0

# Create a masked image of the original image
texture2 = I . copy ()
texture2 [ Mask2 != 0] = 0

# Display the texture images
cv2.imshow("Texture 2", texture2)

# Wait for user input
cv2.waitKey(0)
