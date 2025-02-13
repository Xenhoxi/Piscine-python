from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        img_1 = ft_load("../img/animal.jpeg")
        sx = 100
        sy = 400
        h = 400
        w = 400
        zoom = img_1[sx:sx + h, sy:sy + w, 0]
        print(f"The shape of image is: {zoom.shape + (1,)} or {zoom.shape}")
        print(zoom.reshape((-1, 1)))
        rotated = np.copy(zoom.reshape(zoom.shape[1], zoom.shape[0]))
        for x in range(zoom.shape[0]):
            for y in range(zoom.shape[1]):
                rotated[y, x] = zoom[x, y]
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap='gray')
        plt.show()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
