from load_image import ft_load

import matplotlib.pyplot as plt
import numpy as np


def main():
    img_1 = ft_load("animal.jpeg")
    sx = 100
    sy = 400
    h = 400
    w = 400
    zoomed = img_1[sx:sx + h, sy:sy + w, 0]
    print(f"The shape of image is: {zoomed.shape + (1,)} or {zoomed.shape}")
    print(zoomed.reshape((-1, 1)))
    rotated = np.copy(zoomed.reshape(zoomed.shape[1], zoomed.shape[0]))
    for x in range(zoomed.shape[0]):
        for y in range(zoomed.shape[1]):
            rotated[y, x] = zoomed[x, y]
    print(f"New shape after Transpose: {rotated.shape}")
    print(rotated)
    plt.imshow(rotated, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
