from gaussian_blur import *
from grayscale import *
import math
from PIL import Image

if __name__ == '__main__':
    img = Image.open('cat.png')
    input_img = np.array(img, dtype=float)

    # filter = np.array([[1, 4, 7, 10, 7, 4, 1],
    #                    [4, 12, 26, 33, 26, 12, 4],
    #                    [7, 26, 55, 71, 55, 26, 7],
    #                    [10, 33, 71, 91, 71, 33, 10],
    #                    [7, 26, 55, 71, 55, 26, 7],
    #                    [4, 12, 26, 33, 26, 12, 4],
    #                    [1, 4, 7, 10, 7, 4, 1]])

    # Kernel used for the gaussian blur
    filter = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    # Convert to grayscale
    gray_input = avg_grayscale(input_img)

    # Apply gaussian filter
    blurred = gaussian_filter(gray_input, filter)

    output_img = Image.fromarray(blurred.astype(np.uint8), 'L')
    output_img.save('cat-blurred.png')
