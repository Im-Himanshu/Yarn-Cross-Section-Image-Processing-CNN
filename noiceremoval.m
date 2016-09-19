

I = imread('Capture.png');

Kaverage = filter2(fspecial('average',3),I)/255;
Kmedian = medfilt2(I);
imshowpair(Kaverage,Kmedian,'montage')