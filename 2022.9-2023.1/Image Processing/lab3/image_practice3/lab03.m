clc
clear
I = imread('yjsp.jpg');
I = rgb2gray(I);

figure

subplot(2,3,1);
imshow(I);
title('Original image');

Iroberts = edge(I,'Roberts');
subplot(2,3,2);
%figure
imshow(~Iroberts);
title('Roberts');

Ipr = edge(I,'Prewitt');
subplot(2,3,3);
%figure
imshow(~Ipr);
title('Prewitt');

Isobel = edge(I,'Sobel');
subplot(2,3,4);
%figure
imshow(~Isobel);
title('Sobel');

Ilog = edge(I,'log');
subplot(2,3,5);
%figure
imshow(~Ilog);
title('L o G');

Iedge = edge(I,'Canny');
subplot(2,3,6);
%figure
imshow(~Iedge);
title('Canny');
