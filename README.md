# Badge Verification and Conversion

This Python script is designed to verify and convert badge images according to specific criteria. It provides functions for checking if a badge image meets size requirements, has nontransparent pixels within a circle, and exhibits colors that give a "happy" feeling. Additionally, the script allows users to convert images of any format to a standardized 512x512 PNG badge.

## Features

- **Badge Verification:**
  - Checks if the image dimensions are 512x512 pixels.
  - Verifies that nontransparent pixels are within a circular region.
  - Ensures the colors of the badge evoke a "happy" feeling.

- **Badge Conversion:**
  - Converts images of any format to a 512x512 PNG badge.

## Requirements

- Python 3
- [OpenCV](https://pypi.org/project/opencv-python/) 
- [NumPy](https://pypi.org/project/numpy/) 

## Installation

1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Install OpenCV: `pip install opencv-python`
3. Install NumPy: `pip install numpy`

## Execution
#### python badge_verification.py

## Functions

#### `verify_badge(image_path)`

Verify if the given badge image meets the specified criteria.

##### Parameters:

- `image_path` (str): The file path of the badge image.

##### Returns:

- `str`: Verification result message.

#### `convert_to_badge(image_path, output_path="converted_badge.png")`

Convert the given image to a 512x512 PNG badge.

##### Parameters:

- `image_path` (str): The file path of the input image.
- `output_path` (str): The file path to save the converted badge. Default is "converted_badge.png".

##### Returns:

- `str`: Conversion result message.

#### `is_inside_circle(image)`

Check if nontransparent pixels in the image are within a circle.

##### Parameters:

- `image` (numpy.ndarray): The badge image with an alpha channel.

##### Returns:

- `bool`: True if all nontransparent pixels are within the circle, False otherwise.

#### `is_inside_circle_point(x, y, center_x, center_y, radius)`

Check if a specific point is inside a circle.

##### Parameters:

- `x` (int): X-coordinate of the point.
- `y` (int): Y-coordinate of the point.
- `center_x` (int): X-coordinate of the circle center.
- `center_y` (int): Y-coordinate of the circle center.
- `radius` (int): Radius of the circle.

##### Returns:

- `bool`: True if the point is inside the circle, False otherwise.

#### `has_happy_colors(image)`

Check if the colors of the badge give a 'happy' feeling.

##### Parameters:

- `image` (numpy.ndarray): The badge image with an alpha channel.

##### Returns:

- `bool`: True if the colors give a 'happy' feeling, False otherwise.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
