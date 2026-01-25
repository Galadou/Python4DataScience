from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        if (not img or img.format not in ("JPG", "JPEG")):
            raise AssertionError("img is not in jpg or jpeg format.")
        img = img.convert("RGB")
        img_np = np.array(img)
        print(f"The shape of image is: {img_np.shape}")
        return img_np
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")
