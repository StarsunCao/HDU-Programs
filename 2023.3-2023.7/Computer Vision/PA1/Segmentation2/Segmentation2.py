import cv2 as cv
import numpy as np


##########################################################################
## Mouse event handler function
# @param[in] event Mouse event id
# @param[in] x X coordinate of the mouse event
# @param[in] y Y coordinate of the mouse event
# @param[in] flags Event flags
# @param[in] param Additional parameters passed to event. In current
#            implementation it is a tuple containing source image in
#            RGB color space, same image in Lab color space and an array
#            to store selected pixel coordinates.
## Mouse event handler function

def MouseHandler(event, x, y, flags, param):
    # Only double click event is processed
    if event != cv.EVENT_LBUTTONDBLCLK:
        return

    # Extract data from parameters
    if param is None:
        return
    I, Ilab, sampleAreas, radius, colorMarksBGR = param

    # Add current double-clicked point to the list
    sampleAreas.append((x, y))

    # Create new image with marked pixel
    I2 = I.copy()
    for pix in sampleAreas:
        cv.circle(I2, pix, radius, (0, 0, 255), 1)
    cv.imshow("Source", I2)

    # Calculate color means
    colorMarks = []
    for pix in sampleAreas:
        # Create a mask for the current pixel location
        mask = np.zeros_like(Ilab[0])
        cv.circle(mask, pix, radius, 255, -1)
        # Calculate the mean values of the a and b channels of the Lab color space within the mask
        a = Ilab[1].mean(where=mask > 0)
        b = Ilab[2].mean(where=mask > 0)
        # Add the mean values to the list of color marks
        colorMarks.append((a, b))
        # Calculate the mean BGR color within the mask and add it to the list
        colorMarksBGR.append(I[mask > 0, :].mean(axis=(0)))

    # Calculate distance and create segmented areas
    labels = np.zeros_like(Ilab[0], dtype=np.uint8)
    for i, pix in enumerate(colorMarks):
        # Calculate the Euclidean distance between each pixel in the Lab color space and the color mark
        d = np.sqrt((Ilab[1] - pix[0])**2 + (Ilab[2] - pix[1])**2)
        # Create a mask for pixels that are within radius distance of the color mark
        labels[d < np.sqrt(2)*radius] = i + 1

    # Show segmented image
    cv.imshow("Segmented", cv.cvtColor(labels*50, cv.COLOR_GRAY2BGR))


## Perform the segmentation in the CIE Lab color space using the nearest neighbor method
# @param[in] fn Image file name
def CIELabSegmentation(fn='yjsp.jpg'):
    # Read an image from file
    I = cv.imread(fn, cv.IMREAD_COLOR)
    if not isinstance(I, np.ndarray) or I.data is None:
        print(f"Error reading file \"{fn}\"")
        return
    cv.imshow("Source", I)

    # Convert to CIE Lab color space
    Ilab = cv.cvtColor(I, cv.COLOR_BGR2LAB)
    Ilab = cv.split(Ilab)

    # Define mouse callback function
    sampleAreas = []
    colorMarksBGR = []
    cv.setMouseCallback("Source", MouseHandler, (I, Ilab, sampleAreas, 10, colorMarksBGR))

    # Start an infinite event processing loop
    while True:
        key = cv.waitKey(20) & 0xFF
        if key == 27:
            break
        elif key == 114:
            cv.destroyAllWindows()
            sampleAreas = []
            colorMarksBGR = []
            cv.imshow("Source", I)
            cv.setMouseCallback("Source", MouseHandler, (I, Ilab, sampleAreas, 10, colorMarksBGR))

    cv.destroyAllWindows()


if __name__ == "__main__":
    CIELabSegmentation("yjsp.jpg")
