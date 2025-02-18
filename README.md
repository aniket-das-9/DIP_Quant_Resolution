🖼 Image Processing Project: Quantization & Spatial Resolution Modification

This project implements Image Quantization and Spatial Resolution Modification for grayscale images. The scripts allow users to:

✅ Reduce the bit depth of an image (Image Quantization).
✅ Reduce the spatial resolution of an image (Spatial Resolution Modification).
✅ Analyze performance metrics (execution time vs. parameter values).
✅ Save results in organized folders automatically.
✅ Generate detailed reports for analysis.

📂 Project Structure:

/project_directory
│── image_quantization.py              # Quantization script
│── spatial_resolution.py              # Spatial resolution script
│── requirements.txt                   # Required dependencies
│── Image_Quantization_Report.pdf      # Detailed report on image quantization
│── Spatial_Resolution_Report.pdf      # Detailed report on spatial resolution
│── results_quantization/              # Stores quantization outputs
│── results_spatial/                    # Stores spatial resolution outputs
│── barbara.bmp                         # Test image 1
│── caman.tif                           # Test image 2
│── Lena-Image.png                      # Test image 3
└── README.md                           # Setup and execution guide

🔧 Setup Instructions:

1️⃣ Install Dependencies
Ensure you have Python 3.7+ installed. Then, install the required packages using:
pip install -r requirements.txt
2️⃣ Ensure Test Images Are Available
Place test images in the same directory as the scripts.
3️⃣ Run the Scripts
Each script processes only one image at a time and saves results.

🖼 Image Quantization:

📌 Running the Script
python image_quantization.py

The script prompts for an image filename (e.g., barbara.bmp).
It applies quantization with bit depths: 1, 2, 4, 6.
The output images are saved in results_quantization/:
{image_name}_quantization_results.png (Comparison image)
{image_name}_performance_plot.png (Execution time plot)

✅ Example Output:

Enter the image filename (e.g., barbara.bmp, caman.tif, Lena-Image.png): barbara.bmp
Processing Image: barbara.bmp
Bit Depth: 1, Execution Time: 0.000521 seconds
Bit Depth: 2, Execution Time: 0.000412 seconds
...
Saved comparison image: results_quantization/barbara_quantization_results.png
Saved performance plot: results_quantization/barbara_performance_plot.png

📉 Spatial Resolution Modification:

📌 Running the Script
python spatial_resolution.py

The script prompts for an image filename (e.g., Lena-Image.png).
It applies spatial resolution reduction factors: 2, 4, 8.
The output images are saved in results_spatial/:
{image_name}_spatial_results.png (Comparison image)
{image_name}_performance_plot.png (Execution time plot)

✅ Example Output:

Enter the image filename (e.g., barbara.bmp, caman.tif, Lena-Image.png): Lena-Image.png
Processing Image: Lena-Image.png
Reduction Factor: 2, Execution Time: 0.000138 seconds
Reduction Factor: 4, Execution Time: 0.000324 seconds
...
Saved comparison image: results_spatial/Lena-Image_spatial_results.png
Saved performance plot: results_spatial/Lena-Image_performance_plot.png

📊 Viewing Results:

1️⃣ Quantization Results (results_quantization/):
barbara_quantization_results.png
barbara_performance_plot.png
2️⃣ Spatial Resolution Results (results_spatial/):
barbara_spatial_results.png
barbara_performance_plot.png

📜 Detailed Reports:

The following reports contain detailed analysis and results:

📄 Image_Quantization_Report.pdf → Covers bit depth reduction effects.
📄 Spatial_Resolution_Report.pdf → Covers resolution reduction effects.
These reports include:

Implementation details & design decisions:

Visual results & comparisons
Performance analysis (execution time vs. parameter values)
Discussion of trade-offs & observations
⚡ Performance Analysis
Each script measures execution time vs. bit depth/reduction factor.
Lower bit depths → Faster execution, but lower image quality.
Higher reduction factors → Faster execution, but increased pixelation.

🛠 Customization:

Modify Bit Depths for Image Quantization
Change the bit_depths list in image_quantization.py:
bit_depths = [1, 2, 4, 6]  # Modify as needed
Modify Reduction Factors for Spatial Resolution
Change the reduction_factors list in spatial_resolution.py:
reduction_factors = [2, 4, 8]  # Modify as needed

🤝 Contributing:

Feel free to add support for color images or alternative quantization methods.
Report any issues via GitHub or contact the project owner.


