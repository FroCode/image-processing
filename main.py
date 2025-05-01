import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Step 2: Print "Hello World"
print("Hello World")

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Das_Schwarze_Quadrat.svg/888px-Das_Schwarze_Quadrat.svg.png?20160209215932"
# Fallback URL if the above fails
fallback_url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"

# Debug: Try downloading the image
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad HTTP responses
    print("Image download successful. Content length:", len(response.content))
except requests.exceptions.RequestException as e:
    print(f"Failed to download image from {url}: {e}")
    print("Trying fallback URL...")
    try:
        response = requests.get(fallback_url)
        response.raise_for_status()
        print("Fallback image download successful. Content length:", len(response.content))
    except requests.exceptions.RequestException as e:
        print(f"Failed to download fallback image: {e}")
        exit(1)

# Debug: Convert response to image array
img_array = np.array(bytearray(response.content), dtype=np.uint8)
print("Image array shape:", img_array.shape)

# Decode the image
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Debug: Check if image loaded correctly
if image is None:
    print("Error: Failed to decode image. Check if the file is a valid image.")
    exit(1)
else:
    print("Image loaded successfully. Shape:", image.shape)

# Save the original image
plt.figure(figsize=(6, 6))
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.axis('off')
plt.savefig('original_image.png', bbox_inches='tight')
plt.close()
print("Original image saved as 'original_image.png'")

# Step 4: Resize the image to 256px width
width = 256
height = int((width / image.shape[1]) * image.shape[0])
resized_image = cv2.resize(image, (width, height))

# Save resized image
plt.figure(figsize=(6, 6))
plt.title("Resized Image (256px width)")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.savefig('resized_image.png', bbox_inches='tight')
plt.close()
print("Resized image saved as 'resized_image.png'")

# Step 5: Print the image array
print("Resized Image Array:")
print(resized_image)

# Step 6 (Optional): Convert to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(6, 6))
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.savefig('grayscale_image.png', bbox_inches='tight')
plt.close()
print("Grayscale image saved as 'grayscale_image.png'")

# Step 7 (Optional): Apply edge detection
edges = cv2.Canny(gray_image, 100, 200)
plt.figure(figsize=(6, 6))
plt.title("Edged Image (Canny)")
plt.imshow(edges, cmap='gray')
plt.axis('off')
plt.savefig('edged_image.png', bbox_inches='tight')
plt.close()
print("Edged image saved as 'edged_image.png'")