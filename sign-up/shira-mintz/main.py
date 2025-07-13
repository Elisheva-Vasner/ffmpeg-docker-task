from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = Image.open("image.jpg").convert("RGB")
data = np.array(img)

# Channel splitting
r = data[:, :, 0].flatten()
g = data[:, :, 1].flatten()
b = data[:, :, 2].flatten()

# drawing
plt.figure(figsize=(10, 5))
plt.hist(r, bins=256, color='red', alpha=0.5, label='Red')
plt.hist(g, bins=256, color='green', alpha=0.5, label='Green')
plt.hist(b, bins=256, color='blue', alpha=0.5, label='Blue')
plt.legend()
plt.title("RGB Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")

print("Histogram saved as histogram.png")
