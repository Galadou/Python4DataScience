import matplotlib.pyplot as plt
from load_image import load_image


def main():
    """
    Load animal.jpeg, display its shape, slice the image to make a zoom,
    and display its shape after the slice. Display the sliced img, in grey.
    """
    try:

        img_np = load_image()
        print(f"The shape of image is: {img_np.shape}")
        print(img_np)

        zoom = img_np[100:500, 400:800, 0:1]

        print(f"New shape after slicing: {zoom.shape} or {zoom.shape[:2]}")
        print(zoom)
        plt.imshow(zoom, cmap='gray')
        plt.show()

    except KeyboardInterrupt as error:
        print(f"{type(error)} : Interrupted.")
    except Exception as error:
        print(f"{type(error)} : {error}")


if __name__ == "__main__":
    main()
