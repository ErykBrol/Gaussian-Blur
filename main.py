from gaussian_blur import *


def sobel_gradient(input):
    Gx = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])

    Gy = np.array([[-1, -1, -1],
                   [0, 0, 0],
                   [1, 1, 1]])

    out = np.zeros((input.shape[0], input.shape[1]), dtype=float)

    input_strided = as_strided(
        input,
        shape=(
            input.shape[0] - Gx.shape[0] + 1,
            input.shape[1] - Gx.shape[1] + 1,
            Gx.shape[0],
            Gx.shape[1],
        ),
        strides=(
            input.strides[0],
            input.strides[1],
            input.strides[0],
            input.strides[1],
        ),
        writeable=False,
    )

    dx = np.zeros(input.shape[0], input.shape[1])
    dy = np.zeros(input.shape[0], input.shape[1])

    # x direction
    for row in input_strided:
        for tile in row:


    # y direction
    for row in input_strided:
        for tile in row:
            multiplied_x = np.dot(Gx, tile)
            multiplied_y = np.dot(Gy, tile)

            sum_x_gradient = np.sum(multiplied_x)
            sum_y_gradient = np.sum(multiplied_y)

            out[j, i] = math.sqrt(math.pow(sum_x_gradient, 2) + math.pow(sum_y_gradient, 2))
            i += 1
        i = 0
        j += 1

    # Threshold
    #out[out < 300] = 0
    out *= 255 / np.max(out)

    return out

if __name__ == '__main__':
    img = Image.open('C:\\Users\\Eryk\\Desktop\\valve.png')
    input_img = np.array(img, dtype=float)
    gray_input = to_grayscale(input_img)

    # filter = np.array([[1, 4, 7, 10, 7, 4, 1],
    #                    [4, 12, 26, 33, 26, 12, 4],
    #                    [7, 26, 55, 71, 55, 26, 7],
    #                    [10, 33, 71, 91, 71, 33, 10],
    #                    [7, 26, 55, 71, 55, 26, 7],
    #                    [4, 12, 26, 33, 26, 12, 4],
    #                    [1, 4, 7, 10, 7, 4, 1]])

    filter = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    #gaussed = gauss_filter(gray_input, filter)
    # for row in gaussed:
    #     print("max: " + str(np.max(row)) + " min: " + str(np.min(row)))

    #ret = sobel_gradient(gray_input)

    dx = ndimage.sobel(gray_input, 0)
    dy = ndimage.sobel(gray_input, 1)

    mag = np.hypot(dx, dy)
    mag *= 255.0 / np.max(mag)

    output_img = Image.fromarray(mag.astype(np.uint8), 'L')
    output_img.save('C:\\Users\\Eryk\\Desktop\\valve-lines-np.png')
