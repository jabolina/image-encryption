import sys

from PIL import Image


class ImageModel:
    def __init__(self, path, save_path, key_path):
        self.save_path = save_path
        self.key_path = key_path
        self.image = Image.open(path)
        self.image = self.image.convert('L')
        self.rgb_matrix = self.image.load()
        self.matrix = [[self.rgb_matrix[i, j] for j in range(self.image.size[1])] for i in range(self.image.size[0])]

    def create_image(self, image, matrix):
        pixels = image.load()

        for i in range(image.size[0]):
            for j in range(image.size[1]):
                pixels[i, j] = matrix[i][j]

        try:
            image.save(self.save_path)
            print('Image saved to ' + self.save_path)
        except Exception as ex:
            print(ex)
            exit(0)
