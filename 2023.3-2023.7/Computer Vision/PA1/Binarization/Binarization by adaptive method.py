
import cv2

# Read the image file "yjsp.jpg" in color mode using the imread() function from OpenCV.
I = cv2.imread("yjsp.jpg", cv2.IMREAD_COLOR)

# Convert the color image "I" to grayscale using the cvtColor() function from OpenCV.
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the grayscale image "Igray" using the adaptiveThreshold() function from OpenCV.
Inew = cv2.adaptiveThreshold(Igray, 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 11, 2)

# Display the binary image using the imshow() function from OpenCV.
cv2.imshow( "Binarization by adaptive method" , Inew)

# Wait for a key press before closing the window.
cv2.waitKey(0)
