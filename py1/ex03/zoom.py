import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import load_image

def main():
    try:

        img_np = load_image()
        print(f"The shape of image is: {img_np.shape}")
        print(img_np)

        result_zoom = img_np[100:500, 400:800, 0:1]

        print(f"New shape after slicing: {result_zoom.shape} or {result_zoom.shape[:2]}")
        print(result_zoom)
        plt.imshow(result_zoom, cmap='gray')
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")

if __name__ == "__main__":
    main()
