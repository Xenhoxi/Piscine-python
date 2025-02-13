import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from a specified path"""
    try:
        img = np.array(plt.imread(path))
        print(f"The shape of image is: {img.shape}")
        return img
    except (FileNotFoundError, AttributeError, Exception) as Error:
        print(Error)
        return (None)
