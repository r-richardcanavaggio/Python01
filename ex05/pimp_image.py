import numpy as np
import matplotlib.pyplot as plt


def ft_invert(data: np.ndarray) -> np.ndarray:
    """Inverts the colors of the image received"""
    arr = data.copy()
    arr = 255 - data
    plt.imshow(arr)
    plt.show()
    return arr


def ft_red(data: np.ndarray) -> np.ndarray:
    """Apply red filter to the image received"""
    arr = data.copy()
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    plt.imshow(arr)
    plt.show()
    return arr


def ft_green(data: np.ndarray) -> np.ndarray:
    """Apply green filter to the image received"""
    arr = data.copy()
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    plt.imshow(arr)
    plt.show()
    return arr


def ft_blue(data: np.ndarray) -> np.ndarray:
    """Apply blue filter to the image received"""
    arr = data.copy()
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    plt.imshow(arr)
    plt.show()
    return arr


def ft_grey(data: np.ndarray) -> np.ndarray:
    """Apply grey filter to the image received"""
    arr = np.dot(data[..., :3], [0.2989, 0.5870, 0.1140])
    plt.imshow(arr, cmap='grey')
    plt.show()
    return arr
