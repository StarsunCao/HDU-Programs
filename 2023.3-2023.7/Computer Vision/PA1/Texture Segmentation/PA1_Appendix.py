import numpy as np
import cv2 as cv

##########################################################################
## Remove small objects from binary image
# @param[in] img Image
# @param[in] dim A mininum size of an area to keep
# @param[int] connectivity Pixel connectivity
# @return An image with components less then dim removed
def bwareaopen(img: np.ndarray, dim: int, conn: int = 8):
  if img.ndim != 2 or img.dtype != np.uint8:
    return None
    
  # Find all connected components
  num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(img, connectivity = conn)
  
  # Check size of all connected components
  for i in range(num_labels):
    # Remove connected components smaller than dim
    if stats[i, cv.CC_STAT_AREA] < dim:
      img[labels == i] = 0
          
  return img
  # End of bwareaopen()

##########################################################################
## Implementation of MATLAB`s imfill(I, 'holes') function
# @param[in] I Image to process
# @return An image with holes removed
def imfillholes(I):
  if I.ndim != 2 or I.dtype != np.uint8:
    return None

  rows, cols = I.shape[0:2]
  mask = I.copy()

  # Fill mask from all horizontal borders
  for i in range(cols):
    if mask[0, i] == 0:
      cv.floodFill(mask, None, (i, 0), 255, 10, 10)
    if mask[rows - 1, i] == 0:
      cv.floodFill(mask, None, (i, rows - 1), 255, 10, 10)
  # Fill mask from all vertical borders
  for i in range(rows):
    if mask[i, 0] == 0:
      cv.floodFill(mask, None, (0, i), 255, 10, 10)
    if mask[i, cols - 1] == 0:
      cv.floodFill(mask, None, (cols - 1, i), 255, 10, 10)
      
  # Use the mask to create a resulting image
  res = I.copy()
  res[mask == 0] = 255

  return res
  # End of imfillholes()

##########################################################################
## Entropy filter
# @param[in] I Input image
# @param[out] Iout Output image
# @param[in] el Structuring element
def entropy(I, el):
  # Check input image data
  if I.ndim != 2 or I.dtype != np.uint8:
    return None

  # Convert to image with border
  el_rows, el_cols = el.shape
  Icopy = cv.copyMakeBorder(I, int((el_rows - 1) / 2), int(el_rows / 2), int((el_cols - 1) / 2), int(el_cols / 2), cv.BORDER_REPLICATE)

  # Initialize output image
  Iout = np.zeros_like(I, dtype=np.float32)

  # Initialize local histogram
  hist = np.full((256), 0)

  # Calculate element size
  count = el.sum()

  # For each image pixel - VERY INEFFECTIVE WITH PYTHON!!!
  I_rows, I_cols = I.shape
  for y in range(I_rows):
    for x in range(I_cols):
      # Calculate local histogram
      for i in range(el_rows):
        for j in range(el_cols):
          if el[i, j]:
            hist[Icopy[y + i, x + j]] = hist[Icopy[y + i, x + j]] + 1

      # Calculate entropy
      val = 0
      for i in range(256):
        if hist[i] > 0:
          val -= hist[i] / count * log2(hist[i] / count)
          hist[i] = 0
      Iout[y, x] = val

  return Iout
  # End of entropy()
