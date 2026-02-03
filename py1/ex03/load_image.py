# import matplotlib
# matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from zoom import zoom

#!Attention, WebAgg serv au lieu du truc natif de python sous linux je crois

def main():
    try:
        img = Image.open("animal.jpeg")
        if (not img or img.format not in ("JPEG")):
            raise AssertionError("img is not in jpg or jpeg format.")
        img = img.convert("RGB")
        img_np = np.array(img)
        print(f"The shape of image is: {img_np.shape}")
        print(img_np)

        result_zoom = zoom(img_np, 1)

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