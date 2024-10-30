from PIL import Image

import numpy as np


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        array_img = np.array(img)
        print(f"The shape of image is: {array_img.shape}")
        print(array_img)
        img_gray = img.convert('L')
        array_gray = np.array(img_gray)
        return array_gray
    except (FileNotFoundError, AttributeError, Exception) as Error:
        print(Error)
