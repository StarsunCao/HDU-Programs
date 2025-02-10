%% Nonlinear Filtering
%非线性滤波
%低通滤波器是线性的，当数字图像中存在正态分布的噪声时，低通滤波器是最优的。
%为了消除脉冲噪声，最好使用非线性滤波器，例如中值滤波器。
clc;
close all;
clear;

X=imread('yjsp.jpg');
I=rgb2gray(X); %I is an Gray image
I_Impulse=imread('noise result\Impulse Noise picture.png');%Impulse noise picture as example
I_Additive=imread('noise result\Additive Noise picture.png');%Additive noise picture as example
I_Multiplicative=imread('noise result\Multiplicative Noise picture.png');%Multiplicative noise picture as example
I_Normal=imread('noise result\Gaussian (Normal) Noise picture.png');%Gaussian (Normal) noise picture as example
I_Quantization=imread('noise result\Quantization Noise picture.png');%Quantization noise picture as example
[numRows,numCols]=size(I);

%% Median Filtering
%中值滤波器

I_ori1=I_Impulse;
I_Median=medfilt2(I_ori1);

figure(2);
subplot(1,2,1);
imshow(I_ori1);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Median);
title('Median Filtering Picture');
imwrite(I_Median,'Nonlinear filtering\Median Filtering picture.png');
saveas(2,'Nonlinear filtering\compare Median Filtering picture.png');

%% Weighted Median Filtering
%加权中值滤波器

m=2;n=3;
I_ori2=I_Impulse;
I_Weighted=medfilt2(I_ori2,[m,n]);

figure(3);
subplot(1,2,1);
imshow(I_ori2);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Weighted);
title('Weighted Median Filtering Picture');
imwrite(I_Weighted,'Nonlinear filtering\Weighted Median Filtering picture.png');
saveas(3,'Nonlinear filtering\compare Weighted Median Filtering picture.png');

%% Adaptive Median Filtering
%自适应中值滤波
S_ori=2;%initial size of window(from 0)
S_max=10;
%the maxium size of window could be determined by yourself,which I choose 10.
%the bigger constant you choose,the longer time you run
I_ori3=I_Impulse;
I_extra=ext(I_ori3,S_ori);
I_adaptive=zeros(numRows,numCols);
A1=0;A2=0;
c=0;d=0;e=0;%debug counters
for x=1:1:numRows
    for y=1:1:numCols
        s=S_ori;%initialize size of window
        while 1
            Z=double(I_extra(x:x+s,y:y+s));
            z_med=median(Z,"all");
            z_max=max(Z,[],"all");
            z_min=min(Z,[],"all");
            A1=z_med-z_min;
            A2=z_med-z_max;
            s_max=min([numRows-x,numCols-y,S_max]);
            c=c+1;
            if A1>0 && A2<0
                B1=Z(1,1)-z_min;
                B2=Z(1,1)-z_max;
                if B1>0 && B2<0
                    I_adaptive(x,y)=Z(1,1);
                    break
                else
                    I_adaptive(x,y)=z_med;
                    d=d+1;
                    break
                end
            else
                if s<s_max
                    s=s+1;
                else
                    I_adaptive(x,y)=Z(1,1);
                    e=e+1;
                    break
                end
            end
        end
    end
end

I_adaptive=uint8(I_adaptive);

figure(4);
subplot(1,2,1);
imshow(I_ori3);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_adaptive);
title('adaptive Filtering Picture');
imwrite(I_adaptive,'Nonlinear filtering\Adaptive Median Filtering picture.png');
saveas(4,'Nonlinear filtering\compare Adaptive Median Filtering picture.png');
%% Rank Filtering
I_ori4 = I_Impulse;
I_Rank1 = ordfilt2(I_ori4,1,ones(3,3));
I_Rank2 = ordfilt2(I_ori4,5,ones(3,3));
I_Rank3 = ordfilt2(I_ori4,9,ones(3,3));

figure(5);
subplot(2,2,1);
imshow(I_ori4);
title('before filtering Picture');
subplot(2,2,2);
imshow(I_Rank1);
title(' Rank Filter(filter rank is 0%)');
subplot(2,2,3);
imshow(I_Rank2);
title(' Rank Filter(filter rank is 50%)');
subplot(2,2,4);
imshow(I_Rank3);
title(' Rank Filter(filter rank is 100%)');
saveas(5,'Nonlinear filtering\compare Rank Filter result.png')

imwrite(I_Rank1,'Nonlinear filtering\Rank Filter(filter rank is 0%) picture.png');
imwrite(I_Rank2,'Nonlinear filtering\Rank Filter(filter rank is 50%) picture.png');
imwrite(I_Rank3,'Nonlinear filtering\Rank Filter(filter rank is 100%) picture.png');
%% Wiener Filtering 

I_ori5 = I_Impulse;
m=8;n=8;
I_Wiener = wiener2(I_ori5,[m n]); 

figure(6);
subplot(1,2,1);
imshow(I_ori5);
title('before filtering Picture');
subplot(1,2,2);
imshow(I_Wiener);
title('Wiener Filtering');            
imwrite(I_Wiener,'Nonlinear filtering\Wiener Filtering picture.png');
saveas(6,'Nonlinear filtering\compare Wiener Filtering picture.png');



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