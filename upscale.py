# from PIL import Image, ImageEnhance, ImageFilter
# import cv2
# import numpy as np

# # Load the image using PIL
# image_path = r'C:\Users\hamza\OneDrive\Desktop\20190630_092101.jpg'  # Replace with your image path
# img = Image.open(image_path)

# # Enhance Sharpness
# sharpness_enhancer = ImageEnhance.Sharpness(img)
# sharpened_img = sharpness_enhancer.enhance(2.0)  # Increase sharpness

# # Enhance Contrast
# contrast_enhancer = ImageEnhance.Contrast(sharpened_img)
# enhanced_img = contrast_enhancer.enhance(1.5)  # Increase contrast

# # Enhance Brightness
# brightness_enhancer = ImageEnhance.Brightness(enhanced_img)
# enhanced_img = brightness_enhancer.enhance(1.2)  # Adjust brightness

# # Convert image to OpenCV format for further enhancements
# opencv_img = np.array(enhanced_img)
# opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGB2BGR)

# # Apply a detailed enhancement using OpenCV's bilateral filter
# # Bilateral filter preserves edges while smoothing the image
# opencv_img = cv2.bilateralFilter(opencv_img, d=9, sigmaColor=75, sigmaSpace=75)

# # Save or display the enhanced image
# cv2.imwrite('enhanced_image.jpg', opencv_img)
# cv2.imshow('Enhanced Image', opencv_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

























import cv2

# Load the image using OpenCV
image_path = 'your_image.jpg'  # Replace with your image path
img = cv2.imread(r'C:\Users\hamza\OneDrive\Desktop\20190630_092101.jpg')

# Specify the scaling factor for super-resolution
scale_factor = 2  # Increase image size by 2x (can be 4, etc.)

# Resize image using bicubic interpolation
resized_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

# Save or display the super-resolved image
cv2.imwrite('high_res_image.jpg', resized_img)
cv2.imshow('High-Resolution Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
