import random

import utils
from PIL import Image
from tqdm import *


class Encryption:
    def __init__(self, image):
        self.image = image
        self.encrypted = Image.new(self.image.image.mode, self.image.image.size)
        self.r_vector = [random.randrange(0, 0xFF) for _ in range(self.encrypted.size[0])]
        self.c_vector = [random.randrange(0, 0xFF) for _ in range(self.encrypted.size[1])]

    def xor_scrambled(self, scrambled, pbar):
        for i in range(len(scrambled)):
            if not bool(i % 2):
                reverse = self.c_vector
                reverse.reverse()
                scrambled[i] = [utils.xor(scrambled[i][j], reverse[j], pbar) for j in range(len(self.c_vector))]
            else:
                scrambled[i] = [utils.xor(scrambled[i][j], self.c_vector[j], pbar) for j in range(len(self.c_vector))]
            pbar.update(1)

        for j in range(len(scrambled[0])):
            col = utils.get_column(scrambled, j)
            if not bool(j % 2):
                reverse = self.r_vector
                reverse.reverse()
                scrambled = utils.set_column(scrambled, j,
                                             [utils.xor(col[i], reverse[i], pbar)
                                              for i in range(len(self.r_vector))])
            else:
                scrambled = utils.set_column(scrambled, j,
                                             [utils.xor(col[i], self.r_vector[i], pbar)
                                              for i in range(len(self.r_vector))])
            pbar.update(1)

        return scrambled

    def encrypt(self):
        print('[+] Starting encryption.')
        scrambled = self.image.matrix

        pbar = tqdm(total=2 * (len(self.r_vector) * len(self.c_vector)) + (len(self.r_vector) + len(self.c_vector)))

        for i in range(len(self.r_vector)):
            ith_row_sum = utils.sum_row(i, scrambled)

            if bool(ith_row_sum % 2):
                scrambled[i] = utils.shift(scrambled[i], self.r_vector[i])
            else:
                scrambled[i] = utils.shift(scrambled[i], -self.r_vector[i])
            pbar.update(1)

        for j in range(len(self.c_vector)):
            # jth_column_sum = utils.sum_column(j, scrambled)
            col = utils.get_column(scrambled, j)
            shifted = utils.shift(col, -self.c_vector[j])
            scrambled = utils.set_column(scrambled, j, shifted)
            pbar.update(1)

        scrambled = self.xor_scrambled(scrambled, pbar)

        pbar.close()
        self.image.create_image(self.encrypted, scrambled)

        f = open(self.image.key_path, 'w')
        f.write(str(self.r_vector) + '\n')
        f.write(str(self.c_vector))
        f.close()
