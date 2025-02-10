clc
clear
figure

%%1.FILTERING
%{
I = imread('@UT7UZ3UP4R0J9[$76F@~OK.jpg');
I = im2gray(I);
t = graythresh(I);
A = imbinarize(I,t);
[numRows,numCols,Layers] = size(A);
    subplot(2,2,1);
imshow(A);
title('object');

B = strel('rectangle',[100 150]);

M = B.Neighborhood;
M(numRows,numCols) = 0;
subplot(2,2,2);
imshow(~M);
title('structural element');

Co = imopen(A,B);
subplot(2,2,3);
imshow(Co);
title('eliminated holes');

Cc = imclose(Co,B);
subplot(2,2,4);
imshow(Cc);
title('eliminated protrusions');


%%2.SPLITTING


I = imread('@UT7UZ3UP4R0J9[$76F@~OK.jpg');
subplot(2,3,1);
imshow(I);
title('source');

I = rgb2gray(I);
t = graythresh(I);
Inew = imbinarize(I,t);
subplot(2,3,2);
imshow(Inew);
title('binarized');

Inew = ~Inew;
subplot(2,3,3);
imshow(Inew);
title('inversed');

BW2 = bwmorph(Inew,'erode',5);
subplot(2,3,4);
imshow(BW2);
title('after erosion');

BW2 = bwmorph(BW2,'thicken',Inf);
subplot(2,3,5);
imshow(BW2);

Inew = ~(Inew & BW2);
subplot(2,3,6);
imshow(Inew);

%}
%%3.WATERSHED SEGMENTATION

rgb = imread('@UT7UZ3UP4R0J9[$76F@~OK.jpg');
subplot(3,4,1);
imshow(rgb);
title('source image');

A = rgb2gray(rgb);
subplot(3,4,2);
imshow(A);
title('grayscale representation');

B = strel('disk',6);
C = imerode(A,B);
Cr = imreconstruct(C,A);
Crd = imdilate(Cr,B);
Crdr = imreconstruct(imcomplement(Crd),imcomplement(Cr));
Crdr = imcomplement(Crdr);
subplot(3,4,3);
imshow(Crdr);
title('filtered image');

fgm = imregionalmax(Crdr);
subplot(3,4,4);
imshow(fgm);
title('calculated fgm');

A2 = A;
A2(fgm) = 255;
subplot(3,4,5);
imshow(A2);
title('applied fgm');

B2 = strel(ones(5,5));
fgm = imclose(fgm,B2);
fgm = imerode(fgm,B2);
fgm = bwareaopen(fgm,20);
A3 = A;
A3(fgm) = 255;
subplot(3,4,6);
imshow(A3);
title('filtered fgm');

bw = imbinarize(Crdr);
subplot(3,4,7);
imshow(bw);
title('binarized image');

D = bwdist(bw);
L = watershed(D);
bgm = L == 0;
subplot(3,4,8);
imshow(bgm);
title('calculated bgm');

hy = fspecial('sobel');
hx = hy';
Ay = imfilter(double(A),hy,'replicate');
Ax = imfilter(double(A),hx,'replicate');
grad = sqrt(Ax.^2 + Ay.^2);
grad = imimposemin(grad,bgm |fgm);
subplot(3,4,9);
imshow(grad);
title('gradient segmentation');

L = watershed(grad);
subplot(3,4,10);
imshow(L);
title('segmented gradient');

A4 = A;
A4(imdilate(L == 0,ones(3,3)) | bgm |fgm) = 255;
subplot(3,4,11);
imshow(A4);
title('segmented image');

Lrgb = label2rgb(L,'jet','w','shuffle');
subplot(3,4,12);
imshow(Lrgb);
title('RGB-representation');

