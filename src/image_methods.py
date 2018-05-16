import sys

from PIL import Image


class ImageModel:
    def __init__(self):
        self.image = Image.open(sys.argv[2])
        self.image = self.image.convert('L')
        self.rgb_matrix = self.image.load()
        self.matrix = [[self.rgb_matrix[i, j] for j in range(self.image.size[1])] for i in range(self.image.size[0])]


def create_image(image, matrix):
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixels[i, j] = matrix[i][j]

    try:
        image.save(sys.argv[3])
        print('Image saved to ' + sys.argv[3])
    except Exception as ex:
        print(ex)
        exit(0)
