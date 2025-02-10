

import cv2
import numpy as np

# Define the Weber function
def weber(i):
  if i<0:
    return 0
  if i>255:
    return 255
  if i<=88:
    return int(20-12*i/88)
  if i<=138:
    return int(0.002*(i-88)*(i-88))
  return int(7*(i-138)/117+13)

# Define the Weber Segmentation function
def WeberSegmentation(fn= "yjsp.jpg",fn_out=None):
  # Read the image
  I=cv2.imread(fn,cv2.IMREAD_COLOR)
  if not isinstance(I,np.ndarray) or I.data==None:
    print("Error reading file \"{}\"".format(fn))
    exit()

  # Show the source image
  cv2.imshow("Source",I)

  # Convert the image to grayscale
  Igray=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
  cv2.imshow("Grayscale",Igray)

  # Initialize the Weber image and the Weber2 image
  Iweber =np.zeros_like(Igray)
  Iweber2=np.zeros_like(Igray)
  n=1

  # Perform Weber segmentation
  while(Iweber==0).any():
    Imin=Igray[Iweber==0].min()
    Iw=weber(Imin)
    n=n+1
    mask=np.logical_and(Igray >=Imin,Igray<=Imin+Iw)
    Iweber[mask]=n
    Iweber2[mask]=Imin
  n=n-1
  Iweber=Iweber-1

  # Show the Weber segmentation image in JET colormap
  cv2.imshow("Weber segmentation JET",cv2.applyColorMap((Iweber.astype(np.float32)*255/(n+1)).astype(np.uint8),cv2.COLORMAP_JET))

  # Show the Weber segmentation image
  cv2.imshow("Weber segmentation",Iweber2)
  cv2.waitKey(0)

# Call the Weber Segmentation function
WeberSegmentation("yjsp.jpg")
