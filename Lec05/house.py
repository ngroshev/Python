def main ():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)



def draw_house(x, y, width, height):
    """
    Function that draws house with full width and heght from the reper point (x, y),
    positioned in the bottom of the base.
    :param x: coordinate x of half of width
    :param y: coordinate y of bottom of base
    :param witdth: full width
    :param height: full height
    :return:
    """
    print('Строим дом...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation (x, y, width, height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height )
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_house_foundation (x, y, width, height):
    pass


def draw_house_walls(x, y, width, height):
    pass


def draw_house_roof(x, y, width, height):
    pass


main()
