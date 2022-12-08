"""
# Image tool:
    ## Conversions:
        [.png,.jpeg,.svg,.webp ....]
    - 
    -
    -
    -


"""
from PIL import Image
from numpy import asarray

class IMGTOOL:
    def __init__(self, image_path: str):
        self.image_path = image_path
        img = Image.open(self.image_path)
        self.img_array = asarray(img)


    def check_type(self):
        # Check the type of image uploaded by user
        ...

    def convert(self, output_format: str):

        if output_format == '.png':
            # Convert the image to PNG format
            pass
        elif output_format == '.jpeg':
            # Convert the image to JPEG format
            pass
        elif output_format == '.svg':
            # Convert the image to SVG format
            pass
        elif output_format == '.webp':
            # Convert the image to WEBP format
            pass
        else:
            # Handle unsupported formats
            pass

