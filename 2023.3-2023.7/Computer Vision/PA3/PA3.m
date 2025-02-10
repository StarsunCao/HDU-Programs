clear
clc

%% step 1: read images
%Read the reference image contalning the object of interest.
I1 = imread ('campus_000.jpg');
figure
I1gray = rgb2gray(I1);
boxImage = I1gray;
subplot(2,2,1);
imshow(I1);
title('Object');
%%
%Read the target image containing a scene.
I2 = imread('campus_003.jpg');
I2gray = rgb2gray(I2);
sceneImage = I2gray;
subplot(2,2,3);
figure;
imshow(I2);
title('Scene');

%% Step 2: Detect Feature Points
%Detect feature points in both images.
boxPoints = detectSURFFeatures (boxImage);
scenePoints = detectSURFFeatures (sceneImage);


% Visualize the strongest feature points found in the reference image.
subplot(2,2,2);
figure;
imshow(I1);
title('Strongest Object Features');
hold on;
plot(selectStrongest (boxPoints, 30));
hold off;

% Visualize the strongest feature. points found in the target image.
subplot(2,2,4);
figure;
imshow(I2);
title('Strongest Scene Features');
hold on;
plot(selectStrongest (scenePoints, 100));
hold off;

%% Step 3: Extract Feature Descriptors
% Extract feature descriptors at the interest points in both images.
[boxFeatures, boxPoints] = extractFeatures (boxImage, boxPoints);
[sceneFeatures, scenePoints] = extractFeatures (sceneImage, scenePoints);

%% Step 4: Find Putative Point Matches
%Match the features using their descriptors.
boxPairs = matchFeatures(boxFeatures, sceneFeatures) ;

%%
%Display putatively matched features.
matchedBoxPoints = boxPoints(boxPairs(:,1),:);
matchedScenePoints = scenePoints(boxPairs(:,2),:);

figure;
subplot(2,1,1);
showMatchedFeatures(I1, I2, matchedBoxPoints, ...
    matchedScenePoints, 'montage');
title( 'Putatively Matched Points (Including outliers)');


%% Step 5: Locate the object in the Scene Using Putative Matches
[tform, inlierIdx] = ...
    estimateGeometricTransform2D(matchedBoxPoints, matchedScenePoints, 'affine');
inlierBoxPoints = matchedBoxPoints (inlierIdx, :);
inlierScenePoints = matchedScenePoints(inlierIdx, :);


%%
% Display the matching point pairs with the outliers removed
subplot(2,1,2);
figure;
showMatchedFeatures(I1,I2,inlierBoxPoints, ...
    inlierScenePoints,'montage');
title('Matched Points (Inliers Only)');

%%
% Get the bounding polygon of the reference image.
boxPolygon = [1, 1;...                        %topleft
    size(boxImage, 2), 1;...                  %topright
    size(boxImage, 2), size(boxImage, 1);...  % bottomright
    1,size(boxImage, 1);...                   % bottomleft
    1,1];                                     %topleft again to close the polyon

%%
% Transform the polygon into the coordinate system of the target lmage.
%The trans formed polygon indicates the location of the object in the scene
newBoxPolygon = transformPointsForward(tform, boxPolygon);


%%
% Display the detected object.
figure;
imshow(I2);
hold on;
line(newBoxPolygon(:, 1), newBoxPolygon(:, 2),'Color', 'r');
title('Detected Box');