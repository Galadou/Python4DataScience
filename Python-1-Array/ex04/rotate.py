import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image


def main():
    """
    Loads an image, crops it to a square, converts it to grayscale,
    and displays it after a manual transposition.
    Print its shape before and after transpose.
    """
    try:
        image_np = load_image()
        img_cut = image_np[100:500, 400:800, 0:1]
        print(f"The shape of image is: {img_cut.shape} or {img_cut.shape[:2]}")
        print(img_cut)

        # Transpose
        height, width, channels = img_cut.shape
        result = np.zeros((width, height, channels), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                result[j][i] = img_cut[i][j]
        result = result[:, :, 0]
        print(f"New shape after Transpose: {result.shape}")
        print(result)
        plt.imshow(result, cmap='gray')
        plt.show()

    except KeyboardInterrupt as error:
        print(f"{type(error)} : Interrupted.")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()
