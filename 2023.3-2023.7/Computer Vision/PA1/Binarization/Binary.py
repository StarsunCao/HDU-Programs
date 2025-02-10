import numpy as np
from PIL import Image

# Load the image as a grayscale image
I = np.array(Image.open("yjsp.jpg").convert('L'))

# Set the threshold value
t = 127

# Apply the thresholding operation
Inew = np.where(I > t, 255, 0).astype('uint8')

# Display the binary image
Image.fromarray(Inew).show()
