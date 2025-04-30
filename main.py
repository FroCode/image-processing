import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO


print("Hello World")

# Download and display a "local" image (simulated in Colab)
# Download the image from the provided Wikimedia URL to simulate a local image
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Das_Schwarze_Quadrat.svg/888px-Das_Schwarze_Quadrat.svg.png?20160209215932"
response = requests.get(url)
img_array = np.array(bytearray(response.content), dtype=np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Display the image using Matplotlib (since Colab doesn't support cv2.imshow)
plt.figure(figsize=(6, 6))
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct colors
plt.axis('off')
plt.show()

# Step 4: Load the same image from the remote URL (already done above)
# For clarity, we'll reuse the same image variable

# Step 5: Resize the image to 256px width while maintaining aspect ratio
width = 256
height = int((width / image.shape[1]) * image.shape[0])  # Calculate proportional height
resized_image = cv2.resize(image, (width, height))

# Display resized image
plt.figure(figsize=(6, 6))
plt.title("Resized Image (256px width)")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Step 6: Print the image array
print("Resized Image Array:")
print(resized_image)

# Step 7 (Optional): Convert resized image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
plt.figure(figsize=(6, 6))
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()

# Step 8 (Optional): Apply edge detection (Canny)
edges = cv2.Canny(gray_image, 100, 200)

# Display edged image
plt.figure(figsize=(6, 6))
plt.title("Edged Image (Canny)")
plt.imshow(edges, cmap='gray')
plt.axis('off')
plt.show()