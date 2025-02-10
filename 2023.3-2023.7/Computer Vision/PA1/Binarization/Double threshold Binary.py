
import cv2

# Load the image
I = cv2.imread("yjsp.jpg",cv2.IMREAD_COLOR)

# Set the threshold values
t1 = 127
t2 = 200

# Convert the image to grayscale
Igray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Apply double threshold binary
ret, Inew = cv2.threshold(Igray, t1, 255,cv2.THRESH_BINARY)

# Display the image
cv2.imshow( "Double threshold Binary" , Inew)
cv2.waitKey(0)
