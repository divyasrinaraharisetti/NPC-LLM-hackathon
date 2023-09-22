import cv2
import pytesseract

# Load the image
image_path = 'matrix_screenshot.png'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve OCR accuracy
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Use adaptive thresholding to convert the image to binary
threshold_img = cv2.adaptiveThreshold(
    blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

# Perform OCR (text recognition) using Tesseract
custom_config = r'--oem 3'  # Use OCR Engine Mode 3 (both standard and LSTM OCR)
recognized_text = pytesseract.image_to_string(threshold_img, config=custom_config)

# Print the recognized text
print('Recognized Text:')
print(recognized_text)

# Show the original image and the preprocessed image
cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
