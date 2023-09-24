import cv2
import numpy as np 
import matplotlib.pyplot as plt 

im = cv2.cvtConvert(im, cv2.COLOR_RGB2HSV)# # im[:, :, N] where N is the channel you need
# 0=H, 1=S, V=2
# let's try to make saturation + 80
im[:, :, 1] += 80# reconvert before display

def augmentation(im, fact=.0):
    if fact > 1:
        fact = 1.0
    # get HSV
    hsv = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    
    # set it to numpy array
    hsv = np.array(hsv)
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    
    # fact * channel
    hsv[:,:,0] = np.where(h*fact <= 255, fact*h, h)
    hsv[:,:,1] = np.where(s*fact <= 255, fact*s, s)
    hsv[:,:,2] = np.where(v*fact <= 255, fact*v, v)
    
    # return hsv and rgb
    return hsv, cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

plt.imshow(cv2.cvtConvert(im, cv2.COLOR_HSV2RGB))
plt.show()