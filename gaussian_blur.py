import numpy as np
from numpy.lib.stride_tricks import as_strided
from PIL import Image


# Expected that kernel is symmetrical (width = height)
# and contains odd number of elements
def gauss_filter(image, kernel):
    # Step 1: Pad with blank pixels so that kernel fits over image evenly
    pad_width = (kernel.shape[0] - 1) // 2
    padded_image = np.pad(image, pad_width, 'constant', constant_values=(0, 0))

    # Step 2: Flip kernel horizontally and vertically
    flipped_kernel = np.fliplr(np.flipud(kernel))

    # Step 3: Get strided matrix from padded_image
    strided_image = as_strided(
        padded_image,
        shape=(
            padded_image.shape[0] - kernel.shape[0] + 1,
            padded_image.shape[1] - kernel.shape[1] + 1,
            kernel.shape[0],
            kernel.shape[1],
        ),
        strides=(
            padded_image.strides[0],
            padded_image.strides[1],
            padded_image.strides[0],
            padded_image.strides[1],
        ),
        writeable=False,
    )

    # Step 4: Multiply the flipped kernel over each of the strided matrix segments, add them up
    #         and save their normalized value in the output matrix. Normalization performed by averaging
    #         over the number of kernel values
    output_image = np.zeros((image.shape[0], image.shape[1]))
    i = 0
    j = 0

    for strided_row in strided_image:
        for tile in strided_row:
            multiplied_tile = np.dot(flipped_kernel, tile)
            output_image[j, i] = np.sum(multiplied_tile) // kernel.shape[0]
            i += 1
        i = 0
        j += 1

    # Step 5: Return filtered image
    return output_image


# Takes an image and makes it grayscale by averaging its rgb values
def to_grayscale(img):
    output = np.zeros((img.shape[0], img.shape[1]))

    i = 0
    j = 0

    for row in img:
        for pixel in row:
            output[j, i] = (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) // 3
            i += 1
        j += 1
        i = 0

    return output
