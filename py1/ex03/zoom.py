import numpy as np


def zoom(img_np: np.array, zoom_coef: int) -> np.array:

        if (zoom_coef < 1):
            raise AssertionError("zoom_coed cannot be less than 1.")
        # array[start_y:end_y, start_x:end_x]
        lenY = img_np.shape[0]
        totalenY = int(lenY / zoom_coef)
        startY = int((lenY / 2) - (totalenY / 2))
        endY = int((lenY / 2) + (totalenY / 2))

        lenX = img_np.shape[1]
        totalenX = int(lenX / zoom_coef)
        startX = int((lenX / 2) - (totalenX / 2))
        endX = int((lenX / 2) + (totalenX / 2))

        result_np = img_np[startY: endY, startX: endX]
        return result_np
