from PIL import Image

import numpy as np


np.set_printoptions(precision=0, suppress=True, )

def ft_load(path: str) -> np.array:
    try:
        img = np.array(Image.open(path))
        print(f"The shape of image is: {img.shape}")
        np.
        return img
    except (FileNotFoundError, AttributeError, Exception) as Error:
        print(Error)
