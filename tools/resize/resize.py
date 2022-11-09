import opencv
from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
"""
## Class to Resize images using Nearest Neighbour Algorith:

# Inputs:
    image_array, image_width, image_height
# Outputs
    new_image_array, new_img_width,new_image_height

"""


# Functions
# def myImageResize(img_array,new_w,new_h,interpoltn):
#     """
#         # Experiment 1: Downsample then upsample using nearest neighbor interpolation.
#     """
#     if interpoltn == 'nearest':
#         new_img = np.array(Image.fromarray(img_array).resize((new_h, new_w), Image.Resampling.NEAREST))
#         from matplotlib import pyplot as plt
#         plt.title(f"Downsampled To Width:{new_w} Height:{new_h} using NN  interpolation") 
#         plt.imshow(new_img,  interpolation='nearest')
#         plt.show()

def myImageResize(img_array,new_w,new_h,interpoltn):
    """
        # Experiment 1: Downsample then upsample using nearest neighbor interpolation.
    """
    if interpoltn == 'nearest':
        new_img_nearest = np.array(Image.fromarray(img_array).resize((new_h, new_w), Image.Resampling.NEAREST))
        return new_img_nearest
    
    if interpoltn == 'bilinear':
        new_img_bilinear = np.array(Image.fromarray(img_array).resize((new_h, new_w), Image.Resampling.BILINEAR))
        return new_img_bilinear

def mybilinear(img_array,new_w,new_h,interpoltn):
    img_bilinear = np.array(Image.fromarray(img_array).resize((new_h, new_w), Image.Resampling.BILINEAR))
    return img_bilinear


def myRMSE(orig_array, up_down_sampled_array):
    """
        # Subtract new array from old array then sqr and get the mean
    """
    return np.sqrt(((up_down_sampled_array - orig_array) ** 2).mean())


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
        
        new_img_nearest = np.array(Image.fromarray(self.image_array).resize((new_h, new_w), Image.Resampling.NEAREST))
        return new_img_nearest