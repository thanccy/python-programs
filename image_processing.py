
import numpy as np

# Create an image as a matrix of pixel values
image = np.array([
    [50, 100, 150, 200],
    [60, 110, 160, 210],
    [70, 120, 170, 220],
    [80, 130, 180, 230]
])

print("Original Image:")
print(image)

# 1. Reshape the image
reshaped_image = image.reshape(2, 8)
print("\nReshaped Image:")
print(reshaped_image)

# 2. Slice a specific region
region = image[1:3, 1:3]
print("\nSliced Region:")
print(region)

# 3. Brightness adjustment using broadcasting
brightness = 30
bright_image = np.clip(image + brightness, 0, 255)
print("\nImage after Brightness Adjustment:")
print(bright_image)


# 4. Matrix multiplication for transformation
small_image = image[:2, :2]

transform = np.array([
    [1, 0],
    [0, 1]
])

transformed_image = np.dot(small_image, transform)

print("\nImage after Matrix Transformation:")
print(transformed_image)
