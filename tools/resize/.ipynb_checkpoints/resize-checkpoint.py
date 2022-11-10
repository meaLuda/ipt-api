import cv2
from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
from typing import Union,List
import matplotlib.pyplot as plt

"""
## Class to Resize images using Nearest Neighbour Algorith:

# Inputs:
    image_array, image_width, image_height
# Outputs
    new_image_array, new_img_width,new_image_height

"""

class ResizeTool:
    def __init__(self,img_array):
        """
            #Assumptions:
                We have used opencv to read the image.
                .i.e. 
                import cv2

                im = cv2.imread('data/src/lena.jpg')

                print(type(im))
                # <class 'numpy.ndarray'>

                print(im.shape)
                print(type(im.shape))
                # (225, 400, 3)
                # <class 'tuple'>
        """
        self.image_array = img_array
    
    def w_h(self):
        # return previouse image width,height and channel
        w,h,channel = self.image_array[:,2]
        return (w,h,channel)

    def resize(self,new_w,new_h):
        new_img_nearest = np.array(Image.fromarray(self.image_array).resize((new_h, new_w), Image.Resampling.BILINEAR))
        return new_img_nearest

    
    def debug_class(self,debug=False):
        """ 
            # A debug function for tools we are creating
            # A plt showing before img and after tool process is complete.
            #  
        """
        # BGR to RGB and flip frame
        # input_image = cv2.imread(local_img_path)
        
        input_image  = self.image_array
        new_image_array = self.resize(256,256)
        #subplot(r,c) provide the no. of rows and columns
        # To debug what is actually fed to network
        image_datas = [input_image,new_image_array]
        if debug:
            f, axarr = plt.subplots(2,2)
            axarr[0,0].imshow(image_datas[0])
            axarr[0,1].imshow(image_datas[1])

            plt.show()
        

if __name__ == "__main__":
    im = cv2.imread("dappod.jpg")
    test = ResizeTool(im)
    test.debug_class(debug=True)