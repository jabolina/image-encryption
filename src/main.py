import sys
import image_methods
import encryption
import decryption

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Arguments must be passed.')
        exit(0)

    if str(sys.argv[1]) == 'encrypt':
        model = image_methods.ImageModel(sys.argv[2], sys.argv[3], sys.argv[4])
        encrypt = encryption.Encryption(model)
        encrypt.encrypt()
    elif str(sys.argv[1]) == 'decrypt':
        model = image_methods.ImageModel(sys.argv[3], sys.argv[2], sys.argv[4])
        decrypt = decryption.Decryption(model)
        decrypt.decryption()
    else:
        print('Command ' + sys.argv[1] + ' not found')
        exit(0)
