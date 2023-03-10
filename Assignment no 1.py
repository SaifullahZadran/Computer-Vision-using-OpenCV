"""Submitted by: Saifullah Zadran
   Registration number: 399546"""

"""Applying the following 2D transformations to the image
Translation, Euclidean, Similarity, affine, Projective"""


#Translation
import cv2
import numpy as np

# Load the image
img = cv2.imread("lena.jpg")

# Define the translation matrix
tx = 50  # translation in x direction
ty = 20  # translation in y direction
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the translation
translated_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Show the original and translated image
cv2.imshow("Translated Image", translated_img)
cv2.waitKey(0)



#Eclidean

img = cv2.imread("lena.jpg")      # Loading an image
height, width = img.shape[:2]
# defining euclidean transformation matrix for theta = 30 and Tx = 200, Ty = 200
# sin(30) = 0.5 and cos(30) = 0.86

mat = np.float32([[0.86, -0.5, 200], [0.5, 0.86, 200]])

result = cv2.warpAffine(img, mat, (width, height))

cv2.imshow('original', img)     # printing the images
cv2.imshow('euclidean', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Similarity

# Load the image
img = cv2.imread('lena.jpg')

# Define the scale factor
scale = 1.0

# Define the rotation angle in degrees
angle = 45

# Define the translation amount in pixels
tx, ty = 50, -30

# Calculate the center of the image
h, w = img.shape[:2]
center = (w / 2, h / 2)

# Define the similarity matrix
M = cv2.getRotationMatrix2D(center, angle, scale)
print(M)
M[0, 2] += tx
M[1, 2] += ty

# Apply the similarity affine transformation
result = cv2.warpAffine(img, M, (w, h))

# Display the original and result images
cv2.imshow('Original Image', img)
cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Affine

# Load the image
img = cv2.imread('lena.jpg')
rows, cols, ch = img.shape

cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)

pts1 = np.float32([[83, 90], [447, 90], [83, 472]])
pts2 = np.float32([[0, 0], [447, 90], [150, 472]])

matrix = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow('original', img)     # printing the images
cv2.imshow('affine', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Projective

# Load the image
img = cv2.imread('lena.jpg')

# Define the four source points
src_pts = np.float32([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]],
                      [0, img.shape[0]]])
# Define the four destination points
dst_pts = np.float32([[0, 0], [img.shape[1] * 0.75, 0],
                      [img.shape[1], img.shape[0]], [0, img.shape[0] * 0.75]])

# Calculate the homography matrix
H, _ = cv2.findHomography(src_pts, dst_pts)

# Apply the homography transformation
result = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))

# Display the original and result images
cv2.imshow('Original Image', img)
cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()