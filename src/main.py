import sys
import image_methods
import encryption

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Arguments must be passed.')
        exit(0)

    model = image_methods.ImageModel()

    if str(sys.argv[1]) == 'encrypt':
        encrypt = encryption.Encryption(model)
        encrypt.encrypt()
    elif str(sys.argv[1]) == 'decrypt':
        pass
    else:
        print('Command ' + sys.argv[1] + ' not found')
        exit(0)
