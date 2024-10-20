#uses OpenCV to take image path and add gray scale, canny edge detection and save to path
import cv2
import numpy as np

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

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_edge_detection(image):
    """Apply Canny edge detection to an image."""
    return cv2.Canny(image, 100, 200)

def save_image(image, output_path):
    """Save an image to the specified path."""
    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")

def main():
    print("Welcome to the OpenCV Image Processing Program!")
    
    # Load image
    image_path = input("Enter the path of the image: ")
    image = load_image(image_path)
    display_image("Original Image", image)

    # Convert to grayscale
    grayscale_image = convert_to_grayscale(image)
    display_image("Grayscale Image", grayscale_image)

    # Apply edge detection
    edges_image = apply_edge_detection(grayscale_image)
    display_image("Edges Image", edges_image)

    # Save processed images
    save_grayscale_path = input("Enter a path to save the grayscale image (e.g., grayscale.jpg): ")
    save_image(grayscale_image, save_grayscale_path)

    save_edges_path = input("Enter a path to save the edges image (e.g., edges.jpg): ")
    save_image(edges_image, save_edges_path)

if __name__ == "__main__":
    main()

import cv2
import numpy as np

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

def convert_to_grayscale(image):
    """Convert an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_edge_detection(image):
    """Apply Canny edge detection to an image."""
    return cv2.Canny(image, 100, 200)

def save_image(image, output_path):
    """Save an image to the specified path."""
    cv2.imwrite(output_path, image)
    print(f"Image saved to {output_path}")

def main():
    print("Welcome to the OpenCV Image Processing Program!")
    
    # Load image
    image_path = input("Enter the path of the image: ")
    image = load_image(image_path)
    display_image("Original Image", image)

    # Convert to grayscale
    grayscale_image = convert_to_grayscale(image)
    display_image("Grayscale Image", grayscale_image)

    # Apply edge detection
    edges_image = apply_edge_detection(grayscale_image)
    display_image("Edges Image", edges_image)

    # Save processed images
    save_grayscale_path = input("Enter a path to save the grayscale image (e.g., grayscale.jpg): ")
    save_image(grayscale_image, save_grayscale_path)

    save_edges_path = input("Enter a path to save the edges image (e.g., edges.jpg): ")
    save_image(edges_image, save_edges_path)

if __name__ == "__main__":
    main()
