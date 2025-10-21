"""
Example script demonstrating how to use color_detection module programmatically
"""

from color_detection import detect_yellow_color, detect_yellow_with_pillow
import cv2
import os


def example_basic_detection():
    """Example: Basic yellow color detection"""
    print("=" * 60)
    print("Example 1: Basic Yellow Color Detection")
    print("=" * 60)
    
    # Create test image first if it doesn't exist
    if not os.path.exists("test_image_opencv.jpg"):
        print("Test image not found. Run create_test_image.py first.")
        return
    
    # Detect yellow color
    original, mask, result = detect_yellow_color(
        "test_image_opencv.jpg",
        "example_output.jpg"
    )
    
    # Calculate statistics
    yellow_pixels = cv2.countNonZero(mask)
    total_pixels = mask.shape[0] * mask.shape[1]
    percentage = (yellow_pixels / total_pixels) * 100
    
    print(f"Image dimensions: {original.shape[1]}x{original.shape[0]}")
    print(f"Yellow pixels: {yellow_pixels}")
    print(f"Total pixels: {total_pixels}")
    print(f"Yellow percentage: {percentage:.2f}%")
    print()


def example_pillow_detection():
    """Example: Using Pillow for image loading"""
    print("=" * 60)
    print("Example 2: Yellow Detection with Pillow")
    print("=" * 60)
    
    if not os.path.exists("test_image_pillow.jpg"):
        print("Test image not found. Run create_test_image.py first.")
        return
    
    # Detect yellow using Pillow for image loading
    original, mask, result = detect_yellow_with_pillow("test_image_pillow.jpg")
    
    # Save result
    cv2.imwrite("example_pillow_output.jpg", result)
    
    # Statistics
    yellow_pixels = cv2.countNonZero(mask)
    total_pixels = mask.shape[0] * mask.shape[1]
    
    print(f"Yellow pixels detected: {yellow_pixels}")
    print(f"Percentage: {(yellow_pixels/total_pixels)*100:.2f}%")
    print(f"Output saved to: example_pillow_output.jpg")
    print()


def example_batch_processing():
    """Example: Process multiple images"""
    print("=" * 60)
    print("Example 3: Batch Processing")
    print("=" * 60)
    
    # List of images to process
    images = [
        "test_image_opencv.jpg",
        "test_image_pillow.jpg"
    ]
    
    results_summary = []
    
    for img_path in images:
        if not os.path.exists(img_path):
            print(f"Skipping {img_path} - file not found")
            continue
        
        # Process each image
        original, mask, result = detect_yellow_color(img_path)
        
        # Calculate statistics
        yellow_pixels = cv2.countNonZero(mask)
        total_pixels = mask.shape[0] * mask.shape[1]
        percentage = (yellow_pixels / total_pixels) * 100
        
        results_summary.append({
            'image': img_path,
            'yellow_pixels': yellow_pixels,
            'percentage': percentage
        })
    
    # Display summary
    print("\nBatch Processing Summary:")
    print("-" * 60)
    for result in results_summary:
        print(f"Image: {result['image']}")
        print(f"  Yellow pixels: {result['yellow_pixels']}")
        print(f"  Percentage: {result['percentage']:.2f}%")
        print()


def example_custom_output():
    """Example: Custom output with annotations"""
    print("=" * 60)
    print("Example 4: Custom Output with Annotations")
    print("=" * 60)
    
    if not os.path.exists("test_image_opencv.jpg"):
        print("Test image not found. Run create_test_image.py first.")
        return
    
    # Detect yellow
    original, mask, result = detect_yellow_color("test_image_opencv.jpg")
    
    # Calculate statistics
    yellow_pixels = cv2.countNonZero(mask)
    total_pixels = mask.shape[0] * mask.shape[1]
    percentage = (yellow_pixels / total_pixels) * 100
    
    # Create annotated version
    annotated = original.copy()
    
    # Add text annotation
    text = f"Yellow: {percentage:.1f}%"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(annotated, text, (10, 30), font, 1, (0, 0, 255), 2)
    
    # Create a highlighted version (original with yellow areas highlighted in green)
    highlighted = original.copy()
    highlighted[mask > 0] = [0, 255, 0]  # Green highlight
    
    # Blend original and highlighted
    blended = cv2.addWeighted(original, 0.7, highlighted, 0.3, 0)
    
    # Save outputs
    cv2.imwrite("annotated_output.jpg", annotated)
    cv2.imwrite("highlighted_output.jpg", blended)
    
    print(f"Annotated image saved to: annotated_output.jpg")
    print(f"Highlighted image saved to: highlighted_output.jpg")
    print(f"Yellow detection: {percentage:.2f}%")
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("Yellow Color Detection - Usage Examples")
    print("=" * 60 + "\n")
    
    # Check if test images exist
    if not os.path.exists("test_image_opencv.jpg") and not os.path.exists("test_image_pillow.jpg"):
        print("No test images found!")
        print("Please run: python create_test_image.py")
        print()
        return
    
    # Run examples
    example_basic_detection()
    example_pillow_detection()
    example_batch_processing()
    example_custom_output()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
