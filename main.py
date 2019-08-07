from gaussian_blur import *

if __name__ == '__main__':
    img = Image.open('C:\\Users\\Eryk\\Desktop\\cat.png')
    input_img = np.array(img)
    gray_input = to_grayscale(input_img)

    filter = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

    filter = filter / np.sum(filter)

    ret = gauss_filter(gray_input, filter)

    output_img = Image.fromarray(ret.astype(np.uint8), 'L')
    output_img.save('C:\\Users\\Eryk\\Desktop\\cat_blurred.png')
