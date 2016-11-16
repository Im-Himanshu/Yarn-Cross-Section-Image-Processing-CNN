import numpy as np
import scipy.misc
import math
from queue import *
from PIL import Image, ImageOps, ImageDraw
import pylab as pl

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#make it binary and do something that is code related
def rgb2gray(rgb):
    ary = np.dot(rgb[..., :3], [1, 0, 0])

    return ary

BckgrndClr = 1.0;
input ='Tryme.png'
img = mpimg.imread(input)  #this will the image of the yarn for which the result are to be calculated
gray = rgb2gray(img)
aryimage = np.array(gray,float); # in this black should be 0
processed = np.ndarray(gray.shape,bool) #boolean will store if processed or not
processed.fill(False)
Indfibre = []; # these two will be the finahandfibrel reult of the below function
ImageforAnn = []

#this function will take out all the closed object one by one save them in the different
# array individually and append in IndFibre as an 2d image
# and that can be used later to colour code later
#Below will save the image in imagANN and Indfibre in 30X30 and full image format
#
# -----------------------------------------------------------------------------------
def Segementation(i,j):
    crntFibre = np.ndarray(gray.shape,float)
    crntFibre.fill(BckgrndClr)
    max =[0,0]   # will store max of x and y
    min = [aryimage.shape[0],aryimage.shape[1]] #will store the min of the x and y
    number = [i,j];
    q = Queue(maxsize=min[0]*min[1])
    q.put(number);
    time = 0
    while q.qsize()>0 :
        time+=1
        crnt = q.get()
        i2 = crnt[0]
        j2 = crnt[1]
        if max[0] < crnt[0] :
            max[0] = crnt[0];
        if max[1] < crnt[1]:
            max[1] = crnt[1];
        if min[0] > crnt[0]:
            min[0] = crnt[0];
        if min[1] > crnt[1]:
            min[1] = crnt[1];
        crntFibre[crnt[0],crnt[1]] = aryimage[crnt[0],crnt[1]];
        for i1 in {-1,0,1}:
            for j1 in {-1,0,1}:
                if (i2 + i1) >= 0 & (j2 + j1) >= 0:
                    q2 = processed[i2+i1,j2+j1];
                    w = aryimage[i2+i1,j2+j1]
                    Notprocessed = not processed[i2+i1,j2+j1];
                    #tr1 = not tr ;
                    NotBackground = str(aryimage[i2+i1,j2+j1]) <= str(.68)
                    if(Notprocessed and NotBackground ):
                        putme = [i2+i1,j2+j1]
                        processed[i2+i1,j2+j1] =True
                        q.put(putme)

    if(time>30):
       Indfibre.append(crntFibre);
       s = "Crntfibre" + str(i) + ".png";
       scipy.misc.imsave(s, crntFibre)
       X1 = min[0] - 5
       x2 = max[0] + 5
       Y1 = min[1] - 5
       y2 = max[1] + 5
       if (X1 < 0 or Y1 < 0):
           Y1 += 5;
           X1 += 5;
       if ((x2 > crntFibre.shape[0]) or (y2 > crntFibre.shape[1])):
           x2 = x2 - 5
           y2 = y2 - 5

       CropedFibre = crntFibre[X1:x2, Y1:y2]
       # Kamka = crntFibre[min[0]:max[0],min[1]:max[1]]
       s = "ANNFeed" +str(1)+".png";
       scipy.misc.imsave(s, CropedFibre)
       catIm = Image.open(s)
       width, height = catIm.size
       Sized = catIm.resize((30, 30)) #as ANN take a image of 30 by 30 each resizign this one
       #catIm.save("reshaped " + str(i)+".png") #don't know any other method to resize so doing this only
       ANNfeed = np.reshape(Sized, (1, 900))
       ANNfeed = np.where(ANNfeed<255,0,1)
       #ANNfeed2 = np.reshape(ANNfeed, (30, 30))
       #scipy.misc.imsave("ANNFEED final"+str(i)+".png", ANNfeed2)
       ImageforAnn.append(ANNfeed)
       return 0

for i in range(0,gray.shape[0]) :
    for j in range(0,gray.shape[1]):
        notprocessed = not processed[i,j]
        notAbackground = (str(aryimage[i, j]) <= str(.67));
        if notprocessed and notAbackground :
            processed[i,j] =True;
            Segementation(i,j)
print("stoper")
#above will save the image in imagANN and Indfibre in 30X30 and full image format
#--------------------------------------------------------------------------------------------------


category = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2] #something like that froom the ANN
def makeColourCodedImage():
#this one will be after the prediction of the label for the Images for ANN
     ColorCodedImage = np.ndarray(gray.shape,int) #boolean will store if processed or not
     ColorCodedImage.fill(0)
     p = 0
     for fibre in Indfibre :
         s = "fibre" + str(p) + ".png";
         scipy.misc.imsave(s, fibre)
         Midimage = np.ndarray(gray.shape, int)  # boolean will store if processed or not
         Midimage.fill(0)
         p = p+1
         value = category[p-1]
         n = fibre.shape[0]
         m = fibre.shape[1]
         for i in range(0,n):
             k = 0;
             strtingvalue = 0
             endvalue = 0;
             for j in range (0,m):
                 var = str(fibre[i, j])
                 Notequal = str(var) != str(BckgrndClr)
                 if Notequal:
                     strtingvalue = j;
                     break
             for j in range(m-1,-1,-1): #means step of -1 upto -1
                 var = str(fibre[i, j])
                 Notequal = str(var) != str(BckgrndClr)
                 if Notequal:
                     endvalue = j;
                     break
             for j in range(strtingvalue,endvalue):
                 #fibre[i, j] = 0;  # or what is the boundary colour
                 Midimage[i,j] = value;

         for j in range(0, m):
             k = 0;
             startingvalue = 0
             endvalue = 0;
             for i in range(0, n):
                 var = str(fibre[i, j])
                 Notequal = str(var) != str(BckgrndClr)
                 if Notequal:
                     startingvalue = i;
                     break
             for i in range(n - 1, -1,-1):
                 var = str(fibre[i, j])
                 Notequal = str(var) != str(BckgrndClr)
                 if Notequal:
                     endvalue = i;
                     break
             for i in range(startingvalue, endvalue):
                 fibre[i, j] = 0;  # or what is the boundary colour
                 Midimage[i, j] += value;

         for i in range(0, n):
             k = 0;
             strtingvalue = 0
             endvalue = 0;
             for j in range(0, m):
                 if (Midimage[i,j] > value):
                     ColorCodedImage[i,j] = value;
                     fibre[i,j] = 0;
                 # else :
                 #     ColorCodedImage[i,j] = BckgrndClr;

         s = "after " + str(p) + ".jpg";
         scipy.misc.imsave(s, fibre)
     return ColorCodedImage

ColorCodedImage = makeColourCodedImage()

#check this it wil lahve two different color

#Colorcoded image will save the value(i.e. its category at the pixel position)
# at the fibre location and it background is 0 so it is different from genral
scipy.misc.imsave("ColorCodedImage.jpg", ColorCodedImage)

def CalCentroid():
    totalX = 0;
    totalY = 0;
    count = 0;
    for i in range(0, gray.shape[0]):
        for j in range(0, gray.shape[1]):
            if(ColorCodedImage[i,j]!= 0 ):
                totalX +=i
                totalY+=j
                count+=1
    return [int(totalX/count),int(totalY/count)]


centroid = CalCentroid()
start = 5;
jump = 3;
centreX = centroid[0];
centreY = centroid[1];
PkgDensity = []
# for i in range(1,steps):
#     im = Image.open('ColorCodedImage.jpg')
#     bigsize = (im.size[0] * 3, im.size[1] * 3)
#     mask = Image.new('L', bigsize, 0)
#     draw = ImageDraw.Draw(mask)
#     radii = start+i*jump
#     draw.ellipse([centreX - radii, centreY - radii, centreX + radii, centreY + radii], fill=255)
#     mask = mask.resize(im.size, Image.ANTIALIAS)
#     im.putalpha(mask)
# lets store the distance of all the pixel from the centre in the array
# individually for all type i.e. 1 and 2
NoofPixel1 = {}
NoofPixel2 = {}
totalPixel = {}
max = 0;
for i in range(0, gray.shape[0]):
    for j in range(0, gray.shape[1]):
        dist = math.sqrt((centroid[0]-i)**2+ (centroid[1]-j)**2)
        PixelRange = int(dist/jump)
        if PixelRange > max:
            max = PixelRange
        Pixelvalue = ColorCodedImage[i,j];
        if(Pixelvalue == 1):
            check = NoofPixel1.get(PixelRange)
            if check == None :
                check = 0;
            NoofPixel1.update({PixelRange:check+1})
        if(Pixelvalue == 2):
            check = NoofPixel2.get(PixelRange)
            if check == None:
                check = 0
            NoofPixel2.update(({PixelRange:check+1}))
        check = totalPixel.get(PixelRange)
        if check == None:
            check = 0
        totalPixel.update(({PixelRange: check + 1}))

e =0
def MAtplotcurve(NofPixel11,NoofPixel22,totalPixel1):
       e = 0
       image2 = Image.open(input)
       draw = ImageDraw.Draw(image2)
       draw.point((centreX, centreY), 'red')
       x = centreX
       y = centreY
       X = []
       Y1 =[]
       Y2 = []
       for i in range(0,max+1):
           r = start+e*jump;
           draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0, 0))
           X.append(i)
           p = NofPixel11.get(i)
           q = NoofPixel22.get(i)
           r = totalPixel1.get(i)
           if p == None :
               p = 0
           if q == None:
               q =0
           if r == None:
               r =1
           Y1.append(float(p/r))
           Y2.append(float(q/r))
       image2.save('test.png')
       pl.plot(X, Y1, 'r')
       pl.plot(X, Y2, 'g')
       # give plot a title
       pl.title("’Plot of y vs.x")
       # make axis labels
       pl.xlabel("xaxis")
       pl.ylabel("yaxis")
       # set axis limits
       pl.xlim(0.0, 9.0)
       pl.ylim(0.0, 1)
       pl.show()
    #check how to crop a circular region in the PIL and jsut do it
MAtplotcurve(NoofPixel1,NoofPixel2,totalPixel)

print("khatam ho gya ")