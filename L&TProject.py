import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("wall2.jpg")
image = cv2.resize(image, (600,400))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
_, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cracks = cv2.bitwise_or(edges, morph)

crack_pixels = np.sum(cracks > 0)

total_pixels = cracks.shape[0] * cracks.shape[1]

defect_density = crack_pixels / total_pixels


if defect_density < 0.01:
    damage = "Minor Damage"
elif defect_density < 0.03:
    damage = "Moderate Damage"
else:
    damage = "Major Damage"

print("Crack Pixels:", crack_pixels)
print("Total Pixels:", total_pixels)
print("Defect Density:", defect_density)
print("Damage Level:", damage)


plt.figure(figsize=(10,6))

plt.subplot(221)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(222)
plt.title("Grayscale")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(223)
plt.title("Edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.subplot(224)
plt.title("Detected Cracks")
plt.imshow(cracks, cmap="gray")
plt.axis("off")

plt.show()