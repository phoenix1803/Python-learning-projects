#uses Numpy to load an image, and apply some NumPy operations

import numpy as np
import cv2

def display_image(title, image):
    """Function to display an image."""
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_image(image_path):
    """Load an image from the specified path."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        exit()
    return image

def scale_image(image, factor):
    """Scale the image by a given factor."""
    return cv2.resize(image, None, fx=factor, fy=factor)

def flip_image(image):
    """Flip the image horizontally."""
    return np.fliplr(image)

def mask_image(image, mask_value):
    """Apply a mask to the image to set all values below a certain threshold to black."""
    mask = image > mask_value
    masked_image = np.zeros_like(image)
    masked_image[mask] = image[mask]
    return masked_image

def main():
    print("Welcome to the NumPy Image Processing Program!")
    
    # Load image
    image_path = input("Enter the path of the image: ")
    image = load_image(image_path)
    display_image("Original Image", image)

    # Scale 
    scale_factor = float(input("Enter scaling factor (e.g., 0.5 for half size): "))
    scaled_image = scale_image(image, scale_factor)
    display_image("Scaled Image", scaled_image)

    # Flip 
    flipped_image = flip_image(image)
    display_image("Flipped Image", flipped_image)

    # Mask 
    mask_value = int(input("Enter mask value (0-255): "))
    masked_image = mask_image(image, mask_value)
    display_image("Masked Image", masked_image)

if __name__ == "__main__":
    main()
