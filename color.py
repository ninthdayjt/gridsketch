# anerkiz 20160907
def color1(val):

    color = (0, 0, 0, 0)

    if val == 0:
        color = (0, 0, 0, 0)
    if val <= 3 and val > 0:
        color = (0, 0, 0, 0)
    elif val > 3 and val <= 5:
        color = (204, 255, 153, 255)
    elif val > 5 and val <= 9:
        color = (1, 204, 255, 255)
    elif val > 9 and val <= 13:
        color = (51, 102, 255, 255)
    elif val > 13 and val <= 25:
        color = (255, 153, 0, 255)
    elif val > 25:
        color = (255, 0, 0, 255)

    return color


def color2(val):

    color = (0, 0, 0, 0)

    if val == 0:
        color = (0, 0, 0, 0)
    if val <= 100 and val > 0:
        color = (0, 0, 255, 255)
    elif val > 100 and val <= 200:
        color = (46, 70, 255, 255)
    elif val > 200 and val <= 300:
        color = (59, 124, 255, 255)
    elif val > 300 and val <= 400:
        color = (56, 179, 255, 255)
    elif val > 400 and val <= 500:
        color = (31, 236, 255, 255)
    elif val > 500 and val <= 600:
        color = (97, 255, 221, 255)
    elif val > 600 and val <= 700:
        color = (158, 255, 169, 255)
    elif val > 700 and val <= 800:
        color = (201, 255, 120, 255)
    elif val > 800 and val <= 900:
        color = (236, 255, 64, 255)
    elif val > 900 and val <= 1000:
        color = (255, 238, 0, 255)
    elif val > 1000 and val <= 1100:
        color = (255, 191, 255, 255)
    elif val > 1100 and val <= 1200:
        color = (255, 140, 0, 255)
    elif val > 1200 and val <= 1300:
        color = (255, 85, 0, 255)
    elif val > 1300:
        color = (255, 0, 0, 255)

    return color
