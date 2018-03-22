
import numpy as np
import time
import random
import _pickle as cPickle
import os
import cv2
from PIL import Image
# set numpy output to something sensible
np.set_printoptions(precision=8, edgeitems=6, linewidth=200, suppress=True)
# libraries required for visualisation:
from IPython.display import SVG, display
import svgwrite
# conda install -c omnia svgwrite=1.1.6 if you don't have this lib
# import our command line tools
import cairosvg
import imageio
#crop images
feature = "eye"
file_num = 0
infolder = feature
outfolder = feature + "_cropped"
infile = feature
outfile = feature
os.makedirs(outfolder)
i = 0
for j in range(0,10):
    for k in range(1,9):
        try:
            inf = infolder+"/"+infile+str(j)+"_"+str(k)+".svg"
            print(inf)
            outf = infolder+"/"+infile+str(j)+"_"+str(k)+".png"
            print(outf)
            cairosvg.svg2png(url=inf, write_to=outf)
            inf = infolder+"/"+infile+str(j)+"_"+str(k)+".png"
            print(inf)
            outf = outfolder+"/"+outfile+"_"+str(i) + ".png"
            print(outf)
            im = cv2.imread(inf)
            mask = im < 200
            # Coordinates of non-black pixels.
            coords = np.argwhere(mask)
            # Bounding box of non-black pixels.
            x0, y0,_ = coords.min(axis=0)
            x1, y1,_ = coords.max(axis=0) + 1   # slices are exclusive at the top
            # Get the contents of the bounding box.
            cropped = im[x0:x1, y0:y1]
            cv2.imwrite(outf,cropped)
            print('wrote')
            i += 1
        except:
            continue
total = i

#make images transparent
file_num = 0
infolder = feature + "_cropped"
outfolder = feature + "_final"
infile = feature + "_"
outfile = feature + "_"
os.makedirs(outfolder)
i = 0
for j in range(0,total):
    try:
        inf = infolder+"/" + infile + str(i)+".png"
        outf = outfolder+"/"+outfile+str(i)+".png"
        img = Image.open(inf)
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        data = np.array(img)
        r1, g1, b1 = 0, 0, 0 # Original value
        r2, g2, b2, a2 = 255, 255, 255, 255 # Value that we want to replace it with
        red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:4][mask] = [r2, g2, b2, a2]
        blue_img = Image.fromarray(data)
        blue_img.save(outf, "PNG")
        i += 1
    except:
        continue

