'''
Author: Ambareesh Ravi
Description: Custom PyTorch Transform to pad black around images
Date: July 19,2020
'''

from PIL import Image, ImageOps

class PasteImageOnBlack(object):
    '''
    Pastes the image on a black image
    Or pads an image with black around
    '''
    def __init__(self, max_width = 400, max_height = 300):
        self.max_width = max_width
        self.max_height = max_height
        self.max_value = max([self.max_width, self.max_height])
        
    def __call__(self, image):
        """
        Args:
            img (PIL Image): Image to be padded

        Returns:
            PIL Image: padded Image
        """
        width, height = image.size
        if width < self.max_width or height < self.max_height:
            width_border = (self.max_value - width) // 2
            height_border = (self.max_value - height) // 2
            image = ImageOps.expand(image, border = (width_border, height_border))
        image = image.resize((self.max_value, self.max_value))
        image = image.convert("RGB")
        return image

    def __repr__(self):
        return self.__class__.__name__ + '(%d, %d)'%(self.max_width, self.max_height)
