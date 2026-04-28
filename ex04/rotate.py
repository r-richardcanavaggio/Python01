from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    zoomed = ft_load("animal.jpeg")
    
    if zoomed is None:
        return

    print(zoomed)
    zoomed = zoomed[100:500, 450:850, :1]

    print(f"New shape after slicing: {zoomed.shape}\n{zoomed}")

    transposed = [[row[i] for row in zoomed] for i in range(len(zoomed[0]))]

    rotated = np.array(transposed)
    plt.imshow(rotated, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
