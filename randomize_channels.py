'''
Author: Ambareesh Ravi
Description: Custom PyTorch Transform to rearrange the channels of an input image tensor
Date: July 19,2020
'''

class RandomizeChannels(object):
    '''
    Pastes the image on a black image
    Or pads an image with black around
    '''
    def __init__(self, p):
        self.channels = [0,1,2]
        self.p = p # probability
        self.items = list(range(int(1 / self.p)))
        self.yes = self.items[:int(len(self.items) * self.p)]
        
    def __call__(self, image):
        """
        Args:
            img (torch.Tensor): input image

        Returns:
            Tensor with rearranged channels
        """
        if np.random.choice(self.items) in self.yes:
            np.random.shuffle(self.channels)
            return image[self.channels]
        else:
            return image

    def __repr__(self):
        return self.__class__.__name__
