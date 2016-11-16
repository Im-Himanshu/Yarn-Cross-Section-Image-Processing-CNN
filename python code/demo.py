# import csv
# # fields=['first','second','third']
# # # with open("document.csv", 'a') as f:
# # #                 writer = csv.writer(f)
# # #                 writer.writerow(fields)
# # #                 f.close();
# # # fd = open('document.csv','a')
# # # fd.write(fields)
# # # fd.close()
# # import csv
# #
# # myfile = open("document.csv", 'a',newline='')
# # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # wr.writerow(fields)
# import  numpy as np
# a = [[1,1,2,3,4]]
# myfile = open("document.csv", 'a',newline='')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(a[0])
# d = np.array(a)
# wr.writerow(d[0])

# import numpy as np
# #from scipy import ndimage
# #import scipy.io as sio
# import scipy.misc
# from queue import *
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
#
# img = mpimg.imread('Tryme.png')
# gray = rgb2gray(img)
# aryimage = np.array(gray); # in this black should be 0
# plt.imshow(gray, cmap = plt.get_cmap('gray'))
# plt.show()
# # print("yahao")
# deletme = 1.0
# deleteme2 = 10
# vr = deleteme2 == deletme
# print(vr)
# a = [1,2,3]
# lst = [a] * 5
# print(lst)
# print(lst[1][0])
# from numpy import ndarray
# import  numpy as np
# a = ndarray((5,6),int)
# b = ndarray(a.shape,bool)
# b.fill(True)
# print(a)
# print(b)

# for increasin the size or decreasing the size of an image
# from PIL import  Image
# catIm = Image.open("Tryme.png")
# width, height = catIm.size
# quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
# quartersizedIm.save('quartersized.png')
# svelteIm = catIm.resize((25, 25))
# svelteIm.save('svelte.png')

#image circular crooping
# from PIL import Image, ImageOps, ImageDraw
# im = Image.open('ColorCodedImage.jpg')
# bigsize = (im.size[0] * 3, im.size[1] * 3)
# mask = Image.new('L', bigsize, 0)
# draw = ImageDraw.Draw(mask)
# #draw.ellipse((40, 40) + bigsize, fill=255)
# centreX= int(im.size[0]/2)+30;
# centreY = int(im.size[1]/2)+50
# radii =50
# draw.ellipse([centreX-radii,centreY-radii,centreX+radii,centreY+radii], fill=255)
# mask = mask.resize(im.size, Image.ANTIALIAS)
# im.putalpha(mask)
# im.save("yahoo3.png")

# from PIL import Image, ImageOps, ImageDraw
#
# size = (128, 128)
# mask = Image.new('L', size, 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((0, 0) + size, fill=255)
# im = Image.open('ColorCodedImage.jpg')
# output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
# output.putalpha(mask)
# output.save('output.png')



# import os,sys
# from PIL import Image
# from scipy.misc import imread
# import numpy as np;
# img = Image.open('handfibre.png').convert('LA')
# img.save('greyscaleyarn.png')
# im = imread("greyscaleyarn.png");
# print("yahoo")

dict = {}
for i in range(0,4):
    dict.update({i:1})
for i in range(0,8):
    j = dict.get(i)
    if j == None:
        j = 0


    dict.update({i:j+1})

print(dict)



