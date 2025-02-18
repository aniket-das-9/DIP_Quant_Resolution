import cv2
import numpy as np
import os
import time
import matplotlib.pyplot as plt

# Ensure the results directory exists
RESULTS_DIR = "results_quantization"
os.makedirs(RESULTS_DIR, exist_ok=True)

def quantize_image(image, bit_depth):
    """
    Performs intensity-level quantization on a grayscale 8-bit image.

    Parameters:
    - image: Input grayscale image (NumPy array with dtype uint8).
    - bit_depth: Target bit depth (1 to 8).

    Returns:
    - Quantized image (NumPy array with dtype uint8).
    """
    if image is None:
        raise ValueError("Error: Image not found or cannot be read. Please check the file path.")

    if image.dtype != np.uint8:
        raise ValueError("Error: Input image must be an 8-bit grayscale image (dtype=uint8).")

    if bit_depth < 1 or bit_depth > 8:
        raise ValueError("Bit depth must be between 1 and 8.")

    levels = 2 ** bit_depth  # Number of quantization levels
    scale_factor = 256 // levels  # Scaling factor

    # Perform quantization
    quantized_image = (image // scale_factor) * scale_factor

    return quantized_image

def measure_execution_time(image, bit_depth, repetitions=1000):
    """
    Measures execution time of the quantization function with high precision.

    Parameters:
    - image: Input grayscale image.
    - bit_depth: Target bit depth (1 to 8).
    - repetitions: Number of times to repeat the function to get an average.

    Returns:
    - Average execution time in seconds.
    """
    start_time = time.perf_counter()
    for _ in range(repetitions):
        quantize_image(image, bit_depth)
    end_time = time.perf_counter()

    return (end_time - start_time) / repetitions  # Average execution time per run

def load_and_quantize(image_path, bit_depths):
    """
    Loads an image, ensures it's 8-bit grayscale, applies quantization for multiple bit depths,
    and analyzes execution time.

    Parameters:
    - image_path: Path to the input grayscale image.
    - bit_depths: List of bit depths to test.

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

    # Measure execution time for different bit depths
    execution_times = []
    quantized_images = []

    for bd in bit_depths:
        execution_time = measure_execution_time(image, bd)
        execution_times.append(execution_time)

        quantized_image = quantize_image(image, bd)
        quantized_images.append(quantized_image)

        print(f"Bit Depth: {bd}, Execution Time: {execution_time:.6f} seconds")

    # Display comparison of original and quantized images and save
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, len(bit_depths) + 1, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original (8-bit)")
    plt.axis('off')
    
    for i, (bd, q_img) in enumerate(zip(bit_depths, quantized_images)):
        plt.subplot(1, len(bit_depths) + 1, i + 2)
        plt.imshow(q_img, cmap='gray')
        plt.title(f'Bit Depth: {bd}')
        plt.axis('off')

    comparison_image_path = os.path.join(RESULTS_DIR, f"{os.path.basename(image_path).split('.')[0]}_quantization_results.png")
    plt.savefig(comparison_image_path)
    plt.show()

    # Plot execution time vs. bit depth and save
    plt.figure(figsize=(8, 5))
    plt.plot(bit_depths, execution_times, marker='o', linestyle='-', color='b')
    plt.xlabel("Bit Depth")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Analysis: Execution Time vs. Bit Depth")
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
        # Test with different bit depths
        bit_depths = [1, 2, 4, 6]

        print(f"\nProcessing Image: {image_file}")
        load_and_quantize(image_file, bit_depths)
