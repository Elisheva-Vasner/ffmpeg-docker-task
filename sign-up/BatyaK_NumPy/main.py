import cv2
import matplotlib.pyplot as plt

# load image
image = cv2.imread('data/flower.jpg')

# Get RGB data from image
blue_color = cv2.calcHist([image], [0], None, [256], [0, 256])
red_color = cv2.calcHist([image], [1], None, [256], [0, 256])
green_color = cv2.calcHist([image], [2], None, [256], [0, 256])

#create 4 histograms, one for each color and one more for all the colors combined
plt.subplot(2, 2, 1)
plt.title("histogram of Blue im the image")
plt.hist(blue_color, color="blue")

plt.subplot(2, 2, 2)
plt.title("histogram of Green im the image")
plt.hist(green_color, color="green")

plt.subplot(2, 2, 3)
plt.title("histogram of Red im the image")
plt.hist(red_color, color="red")

#create the combined histogram
plt.subplot(2, 2, 4)
plt.title("Histogram of all RGB Colors")
plt.hist(blue_color, color="blue")
plt.hist(green_color, color="green")
plt.hist(red_color, color="red")

plt.tight_layout()
plt.savefig('data/save/histPic.png')