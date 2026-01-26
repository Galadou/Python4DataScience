import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from zoom import zoom

#!Attention, WebAgg serv au lieu du truc natif de python sous linux je crois

def main():
    # your tests and your error handling
    try:
        img = Image.open("animal.jpeg")
        if (not img or img.format not in ("JPG", "JPEG")):
            raise AssertionError("img is not in jpg or jpeg format.")
        img = img.convert("RGB")
        img_np = np.array(img)
        print(f"The shape of image is: {img_np.shape}")
        print(img_np)

        result_zoom = zoom(img_np, 1)
        plt.imshow(result_zoom, cmap='gray')
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")



if __name__ == "__main__":
    main()