%% Noises Types

clc;
close all;
clear;
X=imread('yjsp.jpg');
I=rgb2gray(X); %I is an Gray image
[numRows,numCols,Layers]=size(I);

figure(1);
imshow(I);
imwrite(I,'noise result\original picture.png');
title('original picture');

%% Impulse Noise
%脉冲噪声：信号因短时间内具有非常大的负值或正值的峰值而失真，并且可能出现解码错误等情况
%会出现白色或黑色的点，被称为噪点。

p=0.1;%p1 is the probability of noise
I_impulse=imnoise(I,'salt & pepper',p);

figure(2);
imshow(I_impulse);
imwrite(I_impulse,'noise result\Impulse Noise picture.png');
title('Impulse Noise Picture');

%% Additive Noise
%加性噪声：噪声影响产生于三个方面，分别是"人为噪声"、"自然噪声"、"内部噪声"
%而这些噪声基本符合某种分布，并且对原图的影响是直接相加，因此称为加性噪声
%我们这里以符合高斯分布的噪声为例

a=0;b=200;% a is mean of noise,b is variance 
Gaussian_noise=a+sqrt(b)*randn(numRows,numCols);%create noise of Gaussian distribution
for m=1:1:numRows
    for n=1:1:numCols
        I_additive(m,n)=I(m,n)+Gaussian_noise(m,n);%add the original pixel with noise
    end
end

figure(3);
imshow(I_additive);
imwrite(I_additive,'noise result\Additive Noise picture.png');
title('Additive Noise Picture');

%% Multiplicative Noise
%乘性噪声：噪声产生与加性噪声类似，只是对原图影响为相乘

I_multiply=imnoise(I,'speckle');

figure(4);
imshow(I_multiply);
imwrite(I_multiply,'noise result\Multiplicative Noise picture.png');
title('Multiplicative Noise Picture');

%% Gaussian (Normal) Noise
%高斯（正态）噪声：正态分布描述略，原理是向原图中添加高斯分布的白噪声

I_Gaussian=imnoise(I,'gaussian',0.001);

figure(5);
imshow(I_Gaussian);
imwrite(I_Gaussian,'noise result\Gaussian (Normal) Noise picture.png');
title('Gaussian (Normal) Noise Picture');

%% Quantization Noise
% 量化噪声：导致物体周围出现虚假轮廓或删除图像中对比度低的细节。
% 量化噪声可以近似地用泊松分布来描述

I_Quantization=imnoise(I,'poisson');

figure(6);
imshow(I_Quantization);
imwrite(I_Quantization,'noise result\Quantization Noise picture.png');
title('Quantization Noise Picture');
