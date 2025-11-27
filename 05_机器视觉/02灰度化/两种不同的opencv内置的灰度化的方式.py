import cv2
import numpy as np

img_color = cv2.imread("flower.png")
gray1 = cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)
gray2 = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

print(np.abs(gray1 - gray2).max())

img = cv2.imread("flower.png", cv2.IMREAD_UNCHANGED)
print(img.shape, img.dtype)

g1 = cv2.imread("flower.png", 0)
g2 = cv2.cvtColor(cv2.imread("flower.png"), cv2.COLOR_BGR2GRAY)
g3 = cv2.cvtColor(cv2.imread("flower.png"), cv2.COLOR_RGB2GRAY)

print("max |g1 - g2| =", np.abs(g1 - g2).max())
print("max |g1 - g3| =", np.abs(g1 - g3).max())
print("max |g2 - g3| =", np.abs(g2 - g3).max())

img = cv2.imread('flower.png')
print("Unique in B:", np.unique(img[:,:,0])[:10])
print("Unique in G:", np.unique(img[:,:,1])[:10])
print("Unique in R:", np.unique(img[:,:,2])[:10])
