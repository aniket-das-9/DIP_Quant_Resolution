import cv2
import numpy as np
import os
import time
import matplotlib.pyplot as plt

# Ensure the results directory exists
RESULTS_DIR = "results_spatial"
os.makedirs(RESULTS_DIR, exist_ok=True)

def reduce_spatial_resolution(image, reduction_factor):
    """
    Reduces the spatial resolution of an image by averaging neighboring pixels.

    Parameters:
    - image: Input grayscale image (NumPy array).
    - reduction_factor: Factor by which to reduce the resolution (2, 4, 8).

    Returns:
    - Resized image with reduced spatial resolution.
    """
    if image is None:
        raise ValueError("Error: Image not found or cannot be read. Please check the file path.")

    if image.dtype != np.uint8:
        raise ValueError("Error: Input image must be an 8-bit grayscale image (dtype=uint8).")

    if reduction_factor < 1:
        raise ValueError("Reduction factor must be >= 1.")

    # Get original image dimensions
    height, width = image.shape

    # Ensure dimensions are divisible by the reduction factor
    new_height = height // reduction_factor
    new_width = width // reduction_factor

    # Resize using block averaging
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    return resized_image

def measure_execution_time(image, reduction_factor, repetitions=100):
    """
    Measures execution time of the spatial resolution reduction function.

    Parameters:
    - image: Input grayscale image.
    - reduction_factor: Factor for resolution reduction.
    - repetitions: Number of times to repeat for averaging execution time.

    Returns:
    - Average execution time in seconds.
    """
    start_time = time.perf_counter()
    for _ in range(repetitions):
        reduce_spatial_resolution(image, reduction_factor)
    end_time = time.perf_counter()

    return (end_time - start_time) / repetitions  # Average execution time per run

def load_and_resize(image_path, reduction_factors):
    """
    Loads an image, ensures it's 8-bit grayscale, applies resolution reduction,
    and analyzes execution time.

    Parameters:
    - image_path: Path to the input grayscale image.
    - reduction_factors: List of reduction factors to test.

    Returns:
    - None (Displays images and execution time plot)
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return

    # Load the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Unable to load image from '{image_path}'. Please check the file format.")
        return

    if image.dtype != np.uint8:
        print(f"Error: Image '{image_path}' is not 8-bit grayscale. Found dtype: {image.dtype}")
        return

    # Measure execution time for different reduction factors
    execution_times = []
    resized_images = []

    for rf in reduction_factors:
        execution_time = measure_execution_time(image, rf)
        execution_times.append(execution_time)

        resized_image = reduce_spatial_resolution(image, rf)
        resized_images.append(resized_image)

        print(f"Reduction Factor: {rf}, Execution Time: {execution_time:.6f} seconds")

    # Display and save comparison image
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, len(reduction_factors) + 1, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original (Full Resolution)")
    plt.axis('off')
    
    for i, (rf, r_img) in enumerate(zip(reduction_factors, resized_images)):
        plt.subplot(1, len(reduction_factors) + 1, i + 2)
        plt.imshow(r_img, cmap='gray')
        plt.title(f'Reduction Factor: {rf}')
        plt.axis('off')

    comparison_image_path = os.path.join(RESULTS_DIR, f"{os.path.basename(image_path).split('.')[0]}_spatial_results.png")
    plt.savefig(comparison_image_path)
    plt.show()

    # Plot execution time vs. reduction factor and save
    plt.figure(figsize=(8, 5))
    plt.plot(reduction_factors, execution_times, marker='o', linestyle='-', color='b')
    plt.xlabel("Reduction Factor")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Analysis: Execution Time vs. Reduction Factor")
    plt.grid(True)

    performance_plot_path = os.path.join(RESULTS_DIR, f"{os.path.basename(image_path).split('.')[0]}_performance_plot.png")
    plt.savefig(performance_plot_path)
    plt.show()

    print(f"\nSaved comparison image: {comparison_image_path}")
    print(f"Saved performance plot: {performance_plot_path}")

if __name__ == "__main__":
    # Ask the user to input the image filename
    image_file = input("Enter the image filename (e.g., barbara.bmp, caman.tif, Lena-Image.png): ").strip()

    # Ensure only one image is taken at a time
    if not os.path.exists(image_file):
        print(f"Error: The file '{image_file}' does not exist. Please check the filename and try again.")
    else:
        # Test with different reduction factors
        reduction_factors = [2, 4, 8]

        print(f"\nProcessing Image: {image_file}")
        load_and_resize(image_file, reduction_factors)
