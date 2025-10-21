"""
Yellow Color Detection using OpenCV
This script detects yellow color in images using HSV color space.
Libraries used: OpenCV, numpy, Pillow
"""

import cv2
import numpy as np
from PIL import Image
import sys
import os


def detect_yellow_color(image_path, output_path=None):
    """
    Detect yellow color in an image using OpenCV.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path to save the output image (optional)
    
    Returns:
        tuple: (original_image, mask, result) - Original image, yellow mask, and result with yellow highlighted
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Could not read image from {image_path}")
    
    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for yellow color in HSV
    # Yellow color typically has H: 20-30, S: 100-255, V: 100-255
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Create a mask for yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Save output if path is provided
    if output_path:
        cv2.imwrite(output_path, result)
        print(f"Result saved to {output_path}")
    
    return image, mask, result


def detect_yellow_with_pillow(image_path):
    """
    Alternative method using Pillow to load image and OpenCV for processing.
    
    Args:
        image_path (str): Path to the input image
    
    Returns:
        tuple: (original_image, mask, result)
    """
    # Load image using Pillow
    pil_image = Image.open(image_path)
    
    # Convert PIL Image to numpy array
    image_array = np.array(pil_image)
    
    # Convert RGB to BGR (OpenCV format)
    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        image = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    else:
        image = image_array
    
    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define yellow color range
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Create mask
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Apply mask
    result = cv2.bitwise_and(image, image, mask=mask)
    
    return image, mask, result


def display_results(original, mask, result, save_comparison=True):
    """
    Display the original image, mask, and result side by side.
    
    Args:
        original: Original image
        mask: Yellow color mask
        result: Result after applying mask
        save_comparison: Whether to save the comparison image
    """
    # Stack images horizontally for comparison
    mask_3channel = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    comparison = np.hstack((original, mask_3channel, result))
    
    # Save comparison image
    if save_comparison:
        comparison_path = "comparison_result.jpg"
        cv2.imwrite(comparison_path, comparison)
        print(f"Comparison image saved to: {comparison_path}")
    
    # Try to display the comparison (may not work in headless environments)
    try:
        import os
        # Check if DISPLAY environment variable is set (indicates GUI availability)
        if os.environ.get('DISPLAY'):
            cv2.imshow('Original | Mask | Yellow Detection Result', comparison)
            print("Press any key to close the window...")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No display available. Results saved to files instead.")
    except Exception as e:
        print(f"Display not available: {str(e)}")


def main():
    """
    Main function to run yellow color detection.
    """
    if len(sys.argv) < 2:
        print("Usage: python color_detection.py <image_path> [output_path]")
        print("Example: python color_detection.py sample.jpg output.jpg")
        return
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "yellow_detected.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    try:
        print(f"Processing image: {image_path}")
        print("Detecting yellow color...")
        
        # Detect yellow color
        original, mask, result = detect_yellow_color(image_path, output_path)
        
        # Calculate statistics
        yellow_pixels = cv2.countNonZero(mask)
        total_pixels = mask.shape[0] * mask.shape[1]
        percentage = (yellow_pixels / total_pixels) * 100
        
        print(f"\nYellow color detection completed!")
        print(f"Yellow pixels detected: {yellow_pixels} ({percentage:.2f}% of image)")
        print(f"Output saved to: {output_path}")
        
        # Display results
        print("\nDisplaying results...")
        display_results(original, mask, result)
        
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
