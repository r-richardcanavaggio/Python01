from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """Opens an image, prints it's shape,
        and returns it's pixel's data in numpy array"""
    try:
        img = Image.open(path)

        if img.format not in ["JPG", "JPEG"]:
            raise ValueError("Wrong format: only JPG and JPEG are supported")
        if img.mode != "RGB":
            raise ValueError("Wrong mode: image must be in RGB")

        data = np.array(img)
        print(f"The shape of image is: {data.shape}")
        return data
    except FileNotFoundError:
        print(f"Error: The file {path} was not found")
        return None
