#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:36:58 2018

@author: root
"""

import numpy as np
import os
import math
from IPython.display import SVG, display
import svgwrite # conda install -c omnia svgwrite=1.1.6
import PIL
from PIL import Image
import svgpathtools # pip install svgpathtools
from svgpathtools import *

def anim_mouth(svg, w=1024.0, h=567.5, num_frames=10):
    
    svg='lips3.svg'
    num_frames=10
    
    paths, attributes, svg_attributes = svg2paths2(svg)
    
    w=float(svg_attributes['width'][:-2])
    h=float(svg_attributes['height'][:-2])
    
    # find inds of corners of mouth
    min_left_ind_start=0
    max_right_ind_end=0
    
    for path in paths:
        i=0
        min_left = w
        max_right = 0
        min_bot = h
        max_top = 0
        d=path.d()
        
        for segment in path:
            x_start=segment.start.real
            x_end=segment.end.real
            if x_start < min_left:
                min_left = x_start
                min_left_ind_start = i
            
            if x_end > max_right:
                max_right = x_end
                max_right_ind_end = i
            
            # find highest and lowest point in obj
            for t in range(0,11,1):           
                y_start=segment.point(t/10).imag
                y_end=segment.point(t/10).imag
                if y_start < min_bot:
                    min_bot = y_start
                
                if y_end > max_top:
                    max_top = y_end
    
            i+=1
    
    # mid of svg object
    mid_y=(min_bot+max_top)/2
    # init mouth corners
    start_left_y=paths[0][min_left_ind_start].start.imag
    end_right_y=paths[0][max_right_ind_end].end.imag
    
    # turn frowns into smles and vice versa
    if start_left_y > mid_y: # frown
        new_left_y=start_left_y-np.minimum(np.maximum((start_left_y-mid_y)*5,mid_y/7),mid_y/3)
    else: # smile
        new_left_y=start_left_y+np.minimum(np.maximum((mid_y-start_left_y)*5,mid_y/7),mid_y/3)
    if end_right_y > mid_y:
        new_right_y=end_right_y-np.minimum(np.maximum((end_right_y-mid_y)*5,mid_y/7),mid_y/3)
    else:
        new_right_y=end_right_y+np.minimum(np.maximum((mid_y-end_right_y)*5,mid_y/7),mid_y/3)
    
    # new mouth corners    
    left_ys=np.linspace(start=start_left_y, stop=new_left_y, num=num_frames+1)
    right_ys=np.linspace(start=end_right_y, stop=new_right_y, num=num_frames+1)
    
    # write new svg files with new mouth corners
    for i in range(num_frames):  
        path_alt = parse_path(d)
        wsvg(path_alt, attributes=attributes, filename='%d_%s' % (i,svg))
        d=d.replace(str(left_ys[i]), str(left_ys[i+1]))
        d=d.replace(str(right_ys[i]), str(right_ys[i+1]))

if __name__ == '__main__':
    
    # iterate files
    for filename in ['lips0','lips1','lips2','lips3']:
        anim_mouth('%s.svg' % filename) 
        
        