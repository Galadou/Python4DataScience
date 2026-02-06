import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import load_image


def main():
    """
    Loads an image, crops it to a square, converts it to grayscale,
    and displays it after a manual transposition.
    """
    try:
        image_np = load_image()
        image_cut = image_np[100:500, 400:800, 0:1]
        print(f"The shape of image is: {image_cut.shape} or {image_cut.shape[:2]}")
        print(image_cut)

        #transpose
        height, width, channels = image_cut.shape
        result = np.zeros((width, height, channels), dtype=np.uint8) # for the moment result got the place but is still empty (with zeros)
        for i in range(height):
            for j in range(width):
                result[j][i] = image_cut[i][j]
        result = result[:, :, 0]
        print(f"New shape after Transpose: {result.shape}")
        print(result)
        plt.imshow(result, cmap='gray')
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()