import cv2
import numpy as np
import matplotlib.pyplot as plt
 
class Hough_line():  
    def __init__(self,num_points=20):
        super(Hough_line, self).__init__()
        self.num_points=num_points
    def voting(self,edge):
        h,w=edge.shape
        max_len=int(np.ceil(np.sqrt(h**2+w**2)))
        hough=np.zeros((max_len,180))
        nonzero_edge_points=np.where(edge>0)
        for (y,x) in zip(nonzero_edge_points[0],nonzero_edge_points[1]):
            for theta in range(0,180):
                t=np.pi/180 * theta
                rho=int(x * np.cos(t) + y * np.sin(t))
                hough[rho,theta]+=1
        return hough.astype(np.uint8)
 
    def NMS(self,hough):
        h,w=hough.shape
        for i in range(h):
            for j in range(w):
                x1=max(i-1,0)
                y1=max(j-1,0)
                x2=min(i+2,h)
                y2=min(j+2,w)
                if(hough[i,j]>0 and np.max(hough[x1:x2,y1:y2])!=hough[i,j]):
                    hough[i,j]=0
        return hough
    def sort_hough(self,hough):
        h,w=hough.shape
        hough_flatten=hough.flatten()
        sort_idxs=np.argsort(hough_flatten)[::-1][:self.num_points]
        rho=sort_idxs//w
        theta=sort_idxs % w
        return rho,theta
    def __call__(self,edge):
        hough=self.voting(edge)
        # hough=self.NMS(hough)
        return self.sort_hough(hough)
 
 
 
if __name__=="__main__":
    img = cv2.imread('1.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
  
    
    lines_detector = Hough_line()
    lines=lines_detector(edges)
    H,W= edges.shape
    for rho, theta in zip(lines[0],lines[1]):
        t=np.pi/180 * theta
        a = np.cos(t)
        b = np.sin(t)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imwrite( "line_result.png", img.astype(float))
    plt.imshow(img)
    #plt.show()
