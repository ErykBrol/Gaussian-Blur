import numpy as np

# Takes an image and makes it grayscale by averaging its rgb values
def avg_grayscale(img):
    output = np.zeros((img.shape[0], img.shape[1]), dtype=float)

    i = 0
    j = 0

    for row in img:
        for pixel in row:
            output[j, i] = (pixel[0] + pixel[1] + pixel[2]) / 3
            i += 1
        j += 1
        i = 0

    return output