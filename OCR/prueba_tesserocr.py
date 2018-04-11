#python 2.7
#-*- encoding UTF-8 -*-

import tesserocr
from PIL import Image

if __name__ == '__main__':
    image1 = Image.open('./frances.jpg')
    # image2 = Image.open('./12.jpg')
    # image3 = Image.open('./13.jpg')
    print tesserocr.image_to_text(image1)
    print('\n')
    # print tesserocr.image_to_text(image2)
    # print('\n')
    # print tesserocr.image_to_text(image3)