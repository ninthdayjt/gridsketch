# anerkiz 20160907
from PIL import Image


def cut(inputImg):

    C = Image.open('assets/china.png')

    width = C.size[0]
    height = C.size[1]

    newImg = Image.new("RGBA", (width + 1, height + 1), (0, 0, 0, 0))

    for i in range(width):
        for j in range(height):
            china = C.getpixel((i, j))
            source = inputImg.getpixel((i, j))

            if china[0] and source[0]:
                newImg.putpixel([i, j], source)

    return newImg