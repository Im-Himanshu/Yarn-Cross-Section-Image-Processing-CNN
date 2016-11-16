rgb = imread('tryme6.png');
I = rgb2gray(rgb);


text(732,501,'Image courtesy of Corel(R)',...
     'FontSize',7,'HorizontalAlignment','right')
hy = fspecial('sobel');
hx = hy';
Iy = imfilter(double(I), hy, 'replicate');
Ix = imfilter(double(I), hx, 'replicate');
gradmag = sqrt(Ix.^2 + Iy.^2);
bc = imcomplement(gradmag);

% read in tiff image and convert it to double format
my_image = im2double(bc);
my_image = my_image(:,:,1);
% perform thresholding by logical indexing
image_thresholded = my_image;
image_thresholded(my_image>-15) = 256;
image_thresholded(my_image<-15) = 0;
% display result
BW = image_thresholded;
BW2 = bwmorph(BW,'remove');
BW3 = imcomplement(BW2);

figure()
subplot(1,2,1)
imshow(BW3,[])
title('original image')                                               
subplot(1,2,2)
imshow(image_thresholded,[])
title('thresholded image')


