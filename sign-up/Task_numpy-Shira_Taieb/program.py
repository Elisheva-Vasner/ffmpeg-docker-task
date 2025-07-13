from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('img_color.png')
img = np.array(img)
if img is None:
    raise ValueError("No image found")

#Divide into 3 matrices containing for each pixel what is the color value
redChannel = img[:, :, 0]
greenChannel = img[:, :, 1]
blueChannel = img[:, :, 2]

histR,_ = np.histogram(redChannel, bins=256, range=(0, 255))
histG,_ = np.histogram(greenChannel, bins=256, range=(0, 255))
histB,_= np.histogram(blueChannel, bins=256, range=(0, 255))

plt.figure(figsize=(10, 6))
plt.plot( np.arange(256) , histR, color='red', label='Red Channel')
plt.plot( np.arange(256) , histG, color='green', label='Green Channel')
plt.plot( np.arange(256) , histB, color='blue', label='Blue Channel')

#Creating the graph
plt.title('RGB Histogram')
plt.xlabel('Color Value (0-255)')
plt.ylabel('Pixel Count')
plt.legend()
plt.grid(True)

#Creating the graph image in the project folder
plt.savefig("output_histogram.png")
print("Histogram saved to output_histogram.png")
print("succeeded!!!!!")