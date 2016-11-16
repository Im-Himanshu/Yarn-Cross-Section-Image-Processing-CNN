RGB = imread('Capture5.png');
% % imshow(RGB);
I = rgb2gray(RGB);
%I = imread('circuit.tif');
threshold = graythresh(I);
bw = im2bw(I,threshold);

BW1 = edge(I,'Canny');
BW2 = edge(I,'Prewitt');
imshowpair(BW1,BW2,'montage');