import cv2 as cv

img = cv.imread('foto/frog.jpg')
cv.imshow('Frog', img)

#averaging
average = cv.blur (img, (3,3))
cv.imshow('Average', average)

#gaussian blur
gauss = cv.GaussianBlur (img, (3,3), 0)
cv.imshow('Gaussian', gauss)

#median blur
median = cv.medianBlur (img, 3)
cv.imshow('Median', median)

#bilateral
bilateral = cv.bilateralFilter (img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)