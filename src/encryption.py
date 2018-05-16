from PIL import Image
from tqdm import *
import image_methods
import random
import utils


class Encryption:
    def __init__(self, image):
        self.image = image
        self.encrypted = Image.new(self.image.image.mode, self.image.image.size)
        self.r_vector = [random.randrange(0, 0xFF) for _ in range(self.encrypted.size[0])]
        self.c_vector = [random.randrange(0, 0xFF) for _ in range(self.encrypted.size[1])]

    def sum_row(self, i):
        value = 0
        for j in range(len(self.image.matrix[i])):
            value += self.image.matrix[i][j]
        return value

    def sum_column(self, j):
        value = 0
        for i in range(len(self.image.matrix[j])):
            value += self.image.matrix[i][j]
        return value

    @staticmethod
    def get_column(matrix, j):
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][j])
        return column

    @staticmethod
    def set_column(matrix, j, column):
        for i in range(len(matrix)):
            matrix[i][j] = column[i]

        return matrix

    def xor_scrambled(self, scrambled, pbar):
        for i in range(len(scrambled)):
            if i == 0 or not bool(2 % i):
                reverse = self.c_vector
                reverse.reverse()
                scrambled[i] = [utils.xor(scrambled[i][j], reverse[j], pbar) for j in range(len(self.c_vector))]
            else:
                scrambled[i] = [utils.xor(scrambled[i][j], self.c_vector[j], pbar) for j in range(len(self.c_vector))]
            pbar.update(1)

        for j in range(len(scrambled[0])):
            if j == 0 or not bool(j % 2):
                reverse = self.r_vector
                reverse.reverse()
                scrambled = self.set_column(scrambled, j,
                                            [utils.xor(self.get_column(scrambled, j)[i], reverse[i], pbar)
                                             for i in range(len(self.r_vector))])
            else:
                scrambled = self.set_column(scrambled, j,
                                            [utils.xor(self.get_column(scrambled, j)[i], self.r_vector[i], pbar)
                                             for i in range(len(self.r_vector))])
            pbar.update(1)

        return scrambled

    def encrypt(self):
        print('[+] Starting encryption.')
        scrambled = self.image.matrix

        pbar = tqdm(total=2*(len(self.r_vector) * len(self.c_vector)) + (len(self.r_vector) + len(self.c_vector)))
        for i in range(len(scrambled)):
            ith_row_sum = self.sum_row(i)

            if bool(ith_row_sum % 2):
                scrambled[i] = utils.shift(self.image.matrix[i], self.r_vector[i])
            else:
                scrambled[i] = utils.shift(self.image.matrix[i], -self.r_vector[i])
            pbar.update(1)

        for j in range(len(scrambled[0])):
            jth_column_sum = self.sum_column(j)

            if bool(jth_column_sum % 2):
                scrambled = self.set_column(scrambled, j,
                                            utils.shift(self.get_column(self.image.matrix, j), self.c_vector[j]))
            else:
                scrambled = self.set_column(scrambled, j,
                                            utils.shift(self.get_column(self.image.matrix, j), -self.c_vector[j]))
            pbar.update(1)

        scrambled = self.xor_scrambled(scrambled, pbar)

        pbar.close()
        image_methods.create_image(self.encrypted, scrambled)
