from quicksort import *
from detect import *

def for_each(limages):
    return [closest_colour(image_rgb(i)) for i in limages]
    
def main(limages):
    lcolours = for_each(limages)
    lnums = colours_to_numbers(lcolours)
    lnums = quicksort(lnums)
    sorted_data = numbers_to_colours(lnums)
    return sorted_data
