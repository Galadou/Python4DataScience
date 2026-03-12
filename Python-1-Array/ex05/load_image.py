from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image, and return it as a numpy.array.

    Args:
        path (str): The path of the image.
    Returns:
        np.array: A 3D array representing the RGB image.
    Raises:
        AssertionError: If the image is not in JPEG format or cannot be opened.
    """
    img = Image.open(path)
    if (not img or img.format not in ("JPEG")):
        raise AssertionError("img is not in jpg or jpeg format.")
    img = img.convert("RGB")
    img_np = np.array(img)
    return img_np
