Custom DataTransforms for PyTorch Dataloaders

This module implements custom PyTorch data transforms to be used with images or video frames
  1. To pad an image with black pixels or zero values based on a maximum resolution and the resolution of the input image
  2. TO randomize the channels of the input images

```python3
# Create objects of the transforms
rand_channels = RandomizeChannels()
pad_transform = PasteImageOnBlack()
```
