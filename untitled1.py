# -*- coding: utf-8 -*-
import numpy 

def polysum(n, s):
    """Return sum of the area and 
    square of the perimeter of the regular polygon."""
    
    area = 0.25 * n * s**2 / numpy.tan(numpy.pi/n)
    prmt = n * s
    final_val = round(float(area + prmt**2), 4)
    return final_val