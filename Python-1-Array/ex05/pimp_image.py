import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.array) -> np.array:
    """
Inverts the color of the image received.
    """
    # Channels with 0 become 255 and conversely, channels with 255 become 0
    img_negatif = 255 - array
    plt.imshow(img_negatif)
    plt.show()
    return img_negatif


def ft_red(array: np.array) -> np.array:
    """
    Put a red filter to the image received.
    """
    red_filter = array.copy()
    red_filter[:, :, 1] = 0
    red_filter[:, :, 2] = 0
    plt.imshow(red_filter)
    plt.show()
    return red_filter


def ft_green(array: np.array) -> np.array:
    """
    Put a green filter to the image received.
    """
    green_filter = array.copy()
    green_filter[:, :, 0] = 0
    green_filter[:, :, 2] = 0
    plt.imshow(green_filter)
    plt.show()
    return green_filter


def ft_blue(array: np.array) -> np.array:
    """
    Put a blue filter to the image received.
    """
    blue_filter = array.copy()
    blue_filter[:, :, 0] = 0
    blue_filter[:, :, 1] = 0
    plt.imshow(blue_filter)
    plt.show()
    return blue_filter


def ft_grey(array: np.array) -> np.array:
    """
    Put a grey filter to the image received.
    """
    np_grey = np.mean(array, axis=2, keepdims=True)
    np_grey = np.repeat(np_grey, 3, axis=2)
    np_grey = np_grey.astype(np.uint8)
    plt.imshow(np_grey)
    plt.show()
    return np_grey
