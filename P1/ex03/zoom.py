from load_image import ft_load

import time
import matplotlib.pyplot as plt
import numpy as np


def main():
    img_1 = ft_load("animal.jpeg")
    sx = 100
    sy = 400
    h = 400
    w = 400
    img_1 = img_1[sx:sx + h, sy:sy + w]
    print(f"New shape after slicing: {np.shape(img_1)}")
    plt.imshow(img_1, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
