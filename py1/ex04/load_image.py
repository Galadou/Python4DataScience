import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def load_image() -> np.array:
    """
    Load animal.jpeg, and return it as a numpy.array.

    Returns:
        np.array: A 3D array representing the RGB image.
    Raises:
        AssertionError: If the image is not in JPEG format or cannot be opened.
    """
    img = Image.open("animal.jpeg")
    if (not img or img.format not in ("JPEG")):
        raise AssertionError("img is not in jpg or jpeg format.")
    img = img.convert("RGB")
    img_np = np.array(img)
    return img_np