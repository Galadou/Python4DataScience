import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from rotate import rotate

def main():
    try:
        img = Image.open("animal.jpeg")
        if (not img or img.format not in ("JPEG")):
            raise AssertionError("img is not in jpeg format.")
        img = img.convert("RGB")
        img_np = np.array(img)
        print(f"The shape of image is: {img_np.shape}")
        print(img_np)

        result_rotate = rotate(img_np)
        print(f"New shape after slicing: {result_rotate.shape} or {result_rotate.shape[:2]}")
        plt.imshow(result_rotate, cmap='gray')
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()