from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey 

import matplotlib.pyplot as plt


array = ft_load("landscape.jpg")
plt.figure(figsize=(10, 8))
plt.subplot(3, 2, 1)
plt.imshow(array)

plt.subplot(3, 2, 2)
plt.imshow(ft_invert(array))

plt.subplot(3, 2, 3)
plt.imshow(ft_red(array))

plt.subplot(3, 2, 4)
plt.imshow(ft_green(array))

plt.subplot(3, 2, 5)
plt.imshow(ft_blue(array))

plt.subplot(3, 2, 6)
plt.imshow(ft_grey(array), cmap='gray')
plt.show()
print(ft_invert.__doc__)
