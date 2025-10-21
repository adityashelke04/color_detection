# Yellow Color Detection using OpenCV

A Python application for detecting yellow color in images using OpenCV, numpy, and Pillow.

## Features

- Detects yellow color in images using HSV color space
- Provides visual output with original image, mask, and detected result
- Supports multiple image formats (JPG, PNG, etc.)
- Command-line interface for easy usage
- Statistics on yellow color detection (percentage of image)

## Libraries Used

- **OpenCV (cv2)**: For image processing and color detection
- **numpy**: For numerical operations and array handling
- **Pillow (PIL)**: For alternative image loading and format support

## Installation

1. Clone this repository:
```bash
git clone https://github.com/adityashelke04/color_detection.git
cd color_detection
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the script with an image file:
```bash
python color_detection.py <image_path> [output_path]
```

### Examples

Detect yellow color in an image:
```bash
python color_detection.py sample_image.jpg
```

Specify custom output path:
```bash
python color_detection.py sample_image.jpg my_output.jpg
```

### Using as a Module

You can also import and use the functions in your own Python scripts:

```python
from color_detection import detect_yellow_color, detect_yellow_with_pillow

# Detect yellow color using OpenCV
original, mask, result = detect_yellow_color("image.jpg", "output.jpg")

# Detect yellow color using Pillow for image loading
original, mask, result = detect_yellow_with_pillow("image.jpg")
```

## How It Works

1. **Image Loading**: The image is loaded using OpenCV or Pillow
2. **Color Space Conversion**: The image is converted from BGR/RGB to HSV color space
3. **Yellow Range Definition**: Yellow color is defined in HSV space:
   - Hue: 20-30
   - Saturation: 100-255
   - Value: 100-255
4. **Mask Creation**: A binary mask is created where yellow pixels are white (255) and others are black (0)
5. **Result Generation**: The mask is applied to the original image to highlight only yellow areas
6. **Display**: Results are shown side-by-side (original, mask, detected result)

## Output

The script provides:
- Visual display of original image, mask, and detection result
- Statistics on yellow pixels detected
- Saved output image with only yellow areas visible

## Requirements

- Python 3.7+
- opencv-python >= 4.8.0
- numpy >= 1.24.0
- Pillow >= 10.0.0

## Color Detection Range

The HSV range for yellow detection can be adjusted in the code:
- `lower_yellow = np.array([20, 100, 100])` - Lower bound
- `upper_yellow = np.array([30, 255, 255])` - Upper bound

You may need to adjust these values based on:
- Lighting conditions in your images
- Specific shade of yellow you want to detect
- Image quality and color accuracy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Aditya Shelke

## Acknowledgments

- OpenCV community for excellent documentation
- Python imaging libraries for making computer vision accessible