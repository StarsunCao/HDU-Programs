%% Images Filtering
%图像滤波:在尽量保留图像细节特征的条件下对目标图像的噪声进行抑制
clc;
close all;
clear;

X=imread('yjsp.jpg');
I=rgb2gray(X); %I is an Gray image
[numRows,numCols]=size(I);

I_Impulse=imread('noise result\Impulse Noise picture.png');%Impulse noise picture as example
I_Additive=imread('noise result\Additive Noise picture.png');%Additive noise picture as example
I_Multiplicative=imread('noise result\Multiplicative Noise picture.png');%Multiplicative noise picture as example
I_Normal=imread('noise result\Gaussian (Normal) Noise picture.png');%Gaussian (Normal) noise picture as example
I_Quantization=imread('noise result\Quantization Noise picture.png');%Quantization noise picture as example

%run this after running p3.m
I_imp_salt=imread('Nonlinear filtering\Adaptive Median Filtering picture.png');

%% Low-pass Filtering
%低通滤波：衰减高通分量(强度变化较大的区域)，保持图像的低通分量不变。用于降低噪声
%有两个主要特点：
%    1. 掩码系数非负
%    2. 所有系数加和为1

%% Arithmetic Mean Filter
%算数均值滤波器
%滤波器将原像素周围的像素进行均值化，计算结果接近原图像。
%由于在几何学中，二维化的滤波器掩码看起来像平行六面体（长方体），因此得名"box-filter"

mask1=fspecial('average',3);
I_Arithmetic=uint8(filter2(mask1,I_Normal));


figure(2);
subplot(1,2,1);
imshow(I_Normal);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Arithmetic);
title('Arithmetic Mean Filter Picture');
imwrite(I_Arithmetic,'Low-pass Filtering\Arithmetic Mean Filter picture.png');
saveas(2,'Low-pass Filtering\compare Arithmetic Mean Filter picture.png');
%% Geometric Mean Filter
%几何均值滤波器
%与算数均值滤波器类似，更适用于失真较轻的图片，抑制高通加性噪声时有更好的性能。
I_Geometric=zeros(numRows,numCols);

%本部分使用的图片预处理函数ext()代码部分在最下面
I_extra1=ext(I_Normal,2);

for x=1:1:numRows
    for y=1:1:numCols
        I_Geometric(x,y)=double(I_extra1(x,y)*I_extra1(x+1,y)*I_extra1(x,y+2)...
            *I_extra1(x+2,y)*I_extra1(x,y+1)*I_extra1(x+1,y+1)*I_extra1(x+2,y+1)...
            *I_extra1(x+1,y+2)*I_extra1(x+2,y+2))^(1/9);
    end
end

I_Geometric=uint8(I_Geometric);

figure(3);
subplot(1,2,1);
imshow(I_Normal);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Geometric);
title('Geometric Mean Filter Picture');
imwrite(I_Geometric,'Low-pass Filtering\Geometric Mean Filter picture.png');
saveas(3,'Low-pass Filtering\compare Geometric Mean Filter picture.png');

%% Harmonic Mean Filter
%谐波均值滤波器

I_extra2=ext(I_imp_salt,2);% if you didn't run p3.m,you can try other noise pictures
onematrix=ones(3,3);

for x=1:1:numRows
    for y=1:1:numCols
        I_Harmonic(x,y)=9/(sum(sum(onematrix./I_extra2(x:x+2,y:y+2))));
    end
end

I_Harmonic=uint8(I_Harmonic);

figure(4);
subplot(1,2,1);
imshow(I_imp_salt);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Harmonic);
title('Harmonic Mean Filter Picture');
imwrite(I_Harmonic,'Low-pass Filtering\Harmonic Mean Filter picture.png');
saveas(4,'Low-pass Filtering\compare Harmonic Mean Filter picture.png');

%% Counterharmonic Mean Filter
%反谐波均值滤波器

I_extra3=ext(I_Normal,2);
Q=0;
%Q > 0 suppresses noises like «pepper»,
%and if Q < 0 — noises like «salt», however, it is not possible to remove
%white and black points at the same time. If Q = 0 the filter turns into
%an arithmetic one, and if Q = −1 — to harmonic.

for Q=-1:1:1
    for x=1:1:numRows
        for y=1:1:numCols
            dividend(x,y)=(sum(sum(I_extra3(x:x+2,y:y+2).^(Q+1))));
            divisor(x,y)=(sum(sum(I_extra3(x:x+2,y:y+2).^Q)));
            I_Counterharmonic(x,y,Q+2)=dividend(x,y)/divisor(x,y);
        end
    end
end
I_Counterharmonic=uint8(I_Counterharmonic);

figure(5);
subplot(2,2,1);
imshow(I_Normal);
title('before filtering Picture');
subplot(2,2,2);
imshow(I_Counterharmonic(:,:,1));
title('Counterharmonic Mean Filter Picture(Q=-1)');
subplot(2,2,3);
imshow(I_Counterharmonic(:,:,2));
title('Counterharmonic Mean Filter Picture(Q=0)');
subplot(2,2,4);
imshow(I_Counterharmonic(:,:,3));
title('Counterharmonic Mean Filter Picture(Q=1)');
imwrite(I_Counterharmonic(:,:,1),'Low-pass Filtering\Counterharmonic Mean Filter picture(Q=-1).png');
imwrite(I_Counterharmonic(:,:,2),'Low-pass Filtering\Counterharmonic Mean Filter picture(Q=0).png')
imwrite(I_Counterharmonic(:,:,3),'Low-pass Filtering\Counterharmonic Mean Filter picture(Q=1).png')
saveas(5,'Low-pass Filtering\compare Counterharmonic Mean Filter picture.png');

%% Gaussian Filter
%高斯滤波器

I_Gaussian=imgaussfilt(I_Normal);

figure(6);
subplot(1,2,1);
imshow(I_Normal);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Gaussian);
title('Gaussian Filter Picture');
imwrite(I_Gaussian,'Low-pass Filtering\Gaussian Filter picture.png')
saveas(6,'Low-pass Filtering\compare Gaussian Filter picture.png');
%% Expand the matrix function

function ext=ext(I_ori,num)%I_ori: original picture;num:extra circle numbers
[numRows,numCols]=size(I_ori);
ext=I_ori;
for x=1:1:num
    [numRows,numCols]=size(ext);
    ext=cat(1,ext,ext(numRows,:));
    ext=cat(2,ext,ext(:,numCols));
end
ext=double(ext);
for x=1:1:numRows
    for y=1:1:numCols
        if ext(x,y)==0
            ext(x,y)=1;
        end
    end
end
end