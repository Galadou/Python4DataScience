import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received.
    """
    # les canaux à 0 deviennt 255 et à l'inverse les 255 deviennent 0
    img_negatif = 255 - array
    print(f"shape invert {img_negatif.shape}")
    plt.imshow(img_negatif)
    plt.show()
    return img_negatif


def ft_red(array: np.array) -> np.array:
    red_filter = array.copy()
    red_filter[:, :, 1] = 0
    red_filter[:, :, 2] = 0
    print(f"shape red {red_filter.shape}")
    plt.imshow(red_filter)
    plt.show()
    return red_filter


def ft_green(array: np.array) -> np.array:
    green_filter = array.copy()
    green_filter[:, :, 0] = 0
    green_filter[:, :, 2] = 0
    print(f"shape green {green_filter.shape}")
    plt.imshow(green_filter)
    plt.show()
    return green_filter


def ft_blue(array: np.array) -> np.array:
    blue_filter = array.copy()
    blue_filter[:, :, 0] = 0
    blue_filter[:, :, 1] = 0
    print(f"shape blue {blue_filter.shape}")
    plt.imshow(blue_filter)
    plt.show()
    return blue_filter


def ft_grey(array: np.array) -> np.array:
    np_grey = np.mean(array, axis=2, keepdims=True)
    np_grey = np.repeat(np_grey, 3, axis=2)
    np_grey = np_grey.astype(np.uint8)
    plt.imshow(np_grey)
    plt.show()
    return np_grey
