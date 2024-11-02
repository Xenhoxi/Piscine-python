from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def main():
    img_1 = ft_load("animal.jpeg")
    sx = 100
    sy = 400
    h = 400
    w = 400
    new = img_1[sx:sx + h, sy:sy + w, 0]
    print(f"The shape of image is: {new.shape + (1,)} or {new.shape}")
    print(new.reshape((-1, 1)))
    new = np.transpose(new)
    print(f"New shape after Transpose: {new.shape}")
    print(new)
    plt.imshow(new, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
