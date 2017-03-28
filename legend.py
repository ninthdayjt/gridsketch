# anerkiz 20160914
from PIL import Image, ImageDraw, ImageFont, ImageFilter

font = ImageFont.truetype(r'assets/Arial.ttf', 18)


def draw(inputImg, flag):

    draw = ImageDraw.Draw(inputImg)

    xoffset, yoffset = 0, 0

    text, colors = [], []

    if flag == 'l1':

        xoffset = 900

        yoffset = 650

        text = ['3-5', '5-9', '9-13', '13-25', '>25']

        colors = [(204, 255, 153), (1, 204, 255), (51, 102, 255), (255, 153, 0), (255, 0, 0)]

    elif flag == 'l2':

        xoffset = 900

        yoffset = 500

        text = ['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000', '1000-1100', '1100-1200', '1200-1300', '>1300']

        colors = [(0, 0, 255), (46, 70, 255), (59, 124, 255), (56, 179, 255), (31, 236, 255), (97, 255, 221), (158, 255, 169), (201, 255, 120), (236, 255, 64), (255, 238, 0), (255, 191, 255), (255, 140, 0), (255, 85, 0), (255, 0, 0)]

    for i in range(len(text)):
        draw.ellipse((xoffset, yoffset + i * 16 + 4, xoffset + 10, yoffset + 14 + i * 16), fill=colors[i])
        draw.text((xoffset + 15, yoffset + i * 16), text[i], font=font, fill=colors[i])

    return inputImg
