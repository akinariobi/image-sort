import cv2
import numpy

HEX_COLOUR = {'#000000': 'black',
             '#808080': 'gray',
             '#ffffff': 'white',
             '#ffa500': 'orange',
             '#ffff00': 'yellow',
             '#008000': 'green',
             '#ee82ee': 'violet',
             '#add8e6': 'lightblue',
             '#90ee90': 'lightgreen',
             '#0000ff': 'blue',
             '#ff0000': 'red'}

COLOUR_NUMBERS = {'red' : 0,
                  'orange' : 1,
                  'yellow' : 2,
                  'lightgreen' : 3,
                  'green' : 4,
                  'lightblue' : 5,
                  'blue' : 6,
                  'violet' : 7,
                  'white' : 8,
                  'gray' : 9,
                  'black' : 10}

def image_rgb(image):
    """ 
    Getting the average colour of an image 
    :return: rgb tuple (r, g, b)
    :rtype: tuple
    """
    img=cv2.imread(image)
    avg_color_per_row = numpy.average(img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    return tuple([round(i) for i in avg_color.tolist()[::-1]])

def hex_to_rgb(hex_colour):
    """
    Converting hex colour to rgb
    :return: rgb tuple (r, g, b)
    :rtype: tuple
    """
    hex_colour=hex_colour[1:]
    return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2 ,4))

def closest_colour(rgb):
    """
    Getting the closest colour (from HEX_COLOUR)
    :return: colour name
    :rtype: string
    """
    min_colours = {}
    for key, value in HEX_COLOUR.items():
        r_c, g_c, b_c = hex_to_rgb(key)
        rd = (r_c - rgb[0]) ** 2
        gd = (g_c - rgb[1]) ** 2
        bd = (b_c - rgb[2]) ** 2
        min_colours[(rd + gd + bd)] = value
    return min_colours[min(min_colours.keys())]

def colours_to_numbers(lcolors):
    """
    Converting list of colours to the list of numbers according to COLOUR_NUMBERS
    :return: list of numbers 
    :rtype: list of int
    """
    return [COLOUR_NUMBERS[i] for i in lcolors]

def numbers_to_colours(alist):
    """
    Converting list of numbers to the list of colours according to COLOUR_NUMBERS
    :return: list of colours
    :rtype: list of str
    """
    return [list(COLOUR_NUMBERS.keys())[list(COLOUR_NUMBERS.values()).index(i)] for i in alist]
