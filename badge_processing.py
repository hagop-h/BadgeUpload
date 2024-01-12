import cv2
import numpy as np

def verify_badge(image_path):
    """
    Verify if the given badge image meets the specified criteria.

    Parameters:
    - image_path (str): The file path of the badge image.

    Returns:
    - str: Verification result message.
    """
    try:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        # Check if the image dimensions are 512x512
        if image.shape[:2] != (512, 512):
            raise ValueError("Badge size is invalid. Please upload a 512x512 image.")

        # Check if nontransparent pixels are within a circle
        if not is_inside_circle(image):
            raise ValueError("Nontransparent pixels should be within a circle.")

        # Check if the colors give a "happy" feeling
        if not has_happy_colors(image):
            raise ValueError("The colors of the badge should give a 'happy' feeling.")

        return "Badge is valid and happy :)."

    except Exception as e:
        return str(e)

def convert_to_badge(image_path, output_path="converted_badge.png"):
    """
    Convert the given image to a 512x512 PNG badge.

    Parameters:
    - image_path (str): The file path of the input image.
    - output_path (str): The file path to save the converted badge. Default is "converted_badge.png".

    Returns:
    - str: Conversion result message.
    """
    try:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        # Resize the image to 512x512
        resized_image = cv2.resize(image, (512, 512))

        # Save the resized image as PNG
        cv2.imwrite(output_path, resized_image)

        return f"Badge successfully converted and saved as {output_path}"

    except Exception as e:
        return str(e)

def is_inside_circle(image):
    """
    Check if nontransparent pixels in the image are within a circle.

    Parameters:
    - image (numpy.ndarray): The badge image with an alpha channel.

    Returns:
    - bool: True if all nontransparent pixels are within the circle, False otherwise.
    """
    try:
        # Calculate the center and radius of the image
        center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
        radius = min(center_x, center_y)

        # Assuming image has an alpha channel (index 3 for the alpha channel)
        alpha_channel = image[:, :, 3]

        # Iterate over pixels and check if nontransparent pixels are inside the circle
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                alpha = alpha_channel[y, x]

                # Check if the pixel is nontransparent and inside the circle
                if alpha > 300 and not is_inside_circle_point(x, y, center_x, center_y, radius):
                    return False

        return True

    except Exception as e:
        return str(e)

def is_inside_circle_point(x, y, center_x, center_y, radius):
    """
    Check if a specific point is inside a circle.

    Parameters:
    - x (int): X-coordinate of the point.
    - y (int): Y-coordinate of the point.
    - center_x (int): X-coordinate of the circle center.
    - center_y (int): Y-coordinate of the circle center.
    - radius (int): Radius of the circle.

    Returns:
    - bool: True if the point is inside the circle, False otherwise.
    """
    return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

def has_happy_colors(image):
    """
    Check if the colors of the badge give a 'happy' feeling.

    Parameters:
    - image (numpy.ndarray): The badge image with an alpha channel.

    Returns:
    - bool: True if the colors give a 'happy' feeling, False otherwise.
    """
    try:
        # Calculate the brightness of each pixel (0.3R + 0.59G + 0.11B)
        brightness = 0.3 * image[:, :, 2] + 0.59 * image[:, :, 1] + 0.11 * image[:, :, 0]

        # Calculate the average brightness of the image
        average_brightness = np.mean(brightness)

        # Define a threshold for darkness (adjust as needed)
        brightness_threshold = 150

        # Check if the average brightness is above the threshold
        return average_brightness > brightness_threshold

    except Exception as e:
        return str(e)

# Example usage:
image_path = "C:/Users/User/Desktop/image.png"

# Verify the badge
verification_result = verify_badge(image_path)
print(verification_result)

# Convert the badge
conversion_result = convert_to_badge(image_path)
print(conversion_result)
