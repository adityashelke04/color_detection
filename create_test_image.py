"""
Test script for yellow color detection
Creates a sample test image with yellow elements
"""

import cv2
import numpy as np
from PIL import Image, ImageDraw


def create_test_image(filename="test_image.jpg"):
    """
    Create a test image with yellow elements for testing color detection.
    
    Args:
        filename (str): Output filename for the test image
    """
    # Create a white background image
    width, height = 800, 600
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Draw yellow shapes
    # Yellow rectangle
    draw.rectangle([50, 50, 250, 200], fill='yellow', outline='black', width=2)
    
    # Yellow circle
    draw.ellipse([300, 50, 500, 250], fill='yellow', outline='black', width=2)
    
    # Yellow polygon (triangle)
    draw.polygon([(550, 200), (650, 50), (750, 200)], fill='yellow', outline='black', width=2)
    
    # Add some non-yellow shapes for comparison
    # Red rectangle
    draw.rectangle([50, 300, 200, 450], fill='red', outline='black', width=2)
    
    # Blue circle
    draw.ellipse([250, 300, 400, 450], fill='blue', outline='black', width=2)
    
    # Green triangle
    draw.polygon([(450, 450), (550, 300), (650, 450)], fill='green', outline='black', width=2)
    
    # Save the image
    image.save(filename)
    print(f"Test image created: {filename}")
    return filename


def create_test_image_opencv(filename="test_image_cv.jpg"):
    """
    Create a test image using OpenCV with yellow elements.
    
    Args:
        filename (str): Output filename for the test image
    """
    # Create a white background
    width, height = 800, 600
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    # Define yellow color in BGR format (OpenCV uses BGR)
    yellow = (0, 255, 255)  # BGR: Blue=0, Green=255, Red=255
    red = (0, 0, 255)
    blue = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    
    # Draw yellow shapes
    # Yellow filled rectangle
    cv2.rectangle(image, (50, 50), (250, 200), yellow, -1)
    cv2.rectangle(image, (50, 50), (250, 200), black, 2)
    
    # Yellow filled circle
    cv2.circle(image, (400, 125), 100, yellow, -1)
    cv2.circle(image, (400, 125), 100, black, 2)
    
    # Yellow filled polygon (triangle)
    pts = np.array([[650, 50], [750, 200], [550, 200]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(image, [pts], yellow)
    cv2.polylines(image, [pts], True, black, 2)
    
    # Add non-yellow shapes
    # Red rectangle
    cv2.rectangle(image, (50, 300), (200, 450), red, -1)
    cv2.rectangle(image, (50, 300), (200, 450), black, 2)
    
    # Blue circle
    cv2.circle(image, (325, 375), 75, blue, -1)
    cv2.circle(image, (325, 375), 75, black, 2)
    
    # Green triangle
    pts2 = np.array([[550, 300], [650, 450], [450, 450]], np.int32)
    pts2 = pts2.reshape((-1, 1, 2))
    cv2.fillPoly(image, [pts2], green)
    cv2.polylines(image, [pts2], True, black, 2)
    
    # Save the image
    cv2.imwrite(filename, image)
    print(f"Test image created using OpenCV: {filename}")
    return filename


if __name__ == "__main__":
    print("Creating test images for yellow color detection...")
    print("\n1. Creating test image using Pillow...")
    create_test_image("test_image_pillow.jpg")
    
    print("\n2. Creating test image using OpenCV...")
    create_test_image_opencv("test_image_opencv.jpg")
    
    print("\nTest images created successfully!")
    print("\nYou can now test the color detection with:")
    print("  python color_detection.py test_image_pillow.jpg")
    print("  python color_detection.py test_image_opencv.jpg")
