import numpy as np

def rotate(image_np: np.ndarray) -> np.ndarray:
    return image_np.transpose(1, 0, 2) #! mayday pas bon faut faire soit meme