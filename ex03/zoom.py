from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    zoomed = ft_load("animal.jpeg")
    
    if zoomed is None:
        return

    print(zoomed)
    zoomed = zoomed[100:500, 450:850, :1]
    print("-------\n")
    print(f"New shape after slicing: {zoomed.shape}\n{zoomed}")

    plt.imshow(zoomed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
