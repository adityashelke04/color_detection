# Quick Start Guide

## Installation
```bash
pip install -r requirements.txt
```

## Basic Usage

### 1. Create Test Images
```bash
python create_test_image.py
```

### 2. Detect Yellow Color
```bash
python color_detection.py test_image_opencv.jpg output.jpg
```

### 3. Run Examples
```bash
python examples.py
```

### 4. Run Tests
```bash
python test_verification.py
```

## Command Line Options

```bash
# Basic detection
python color_detection.py <input_image> [output_image]

# Examples:
python color_detection.py photo.jpg                    # Output: yellow_detected.jpg
python color_detection.py photo.jpg my_result.jpg      # Output: my_result.jpg
```

## Programmatic Usage

```python
from color_detection import detect_yellow_color

# Detect yellow in an image
original, mask, result = detect_yellow_color("image.jpg", "output.jpg")

# Get statistics
import cv2
yellow_pixels = cv2.countNonZero(mask)
total_pixels = mask.shape[0] * mask.shape[1]
percentage = (yellow_pixels / total_pixels) * 100
print(f"Yellow: {percentage:.2f}%")
```

## Output Files

After running detection, you'll get:
- **output.jpg** - Image with only yellow areas visible
- **comparison_result.jpg** - Side-by-side comparison (original | mask | result)

## Adjusting Yellow Range

Edit `color_detection.py` to change HSV thresholds:
```python
# Current values (good for bright yellow)
lower_yellow = np.array([20, 100, 100])  # H, S, V
upper_yellow = np.array([30, 255, 255])

# For lighter yellow:
lower_yellow = np.array([15, 50, 50])
upper_yellow = np.array([35, 255, 255])

# For darker yellow:
lower_yellow = np.array([20, 150, 100])
upper_yellow = np.array([30, 255, 200])
```

## HSV Color Space Reference

- **Hue (H)**: 0-180 in OpenCV (yellow is around 20-30)
- **Saturation (S)**: 0-255 (0 = grayscale, 255 = pure color)
- **Value (V)**: 0-255 (0 = black, 255 = bright)

## Troubleshooting

### No yellow detected
- Check if image actually contains yellow
- Adjust HSV range values
- Try converting image to different format

### Import errors
```bash
pip install --upgrade -r requirements.txt
```

### Display errors (headless environment)
- Normal behavior - results saved to files
- Use comparison_result.jpg to view results
