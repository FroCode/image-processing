Image Processing Assignment
This repository contains the solution for Task #1 - Basics of Image Processing


Load and display a local image (simulated via download in this case).
Load an image from a remote URL (Wikimedia Commons).
Resize the image to a width of 256 pixels.
Print the image array.
Convert the resized image to grayscale (optional).
Apply edge detection to the resized image (optional).

The code is implemented in main.py and produces four output images (original_image.png, resized_image.png, grayscale_image.png, edged_image.png) to demonstrate the processing steps.
Files

main.py: The main Python script implementing the assignment requirements.
original_image.png: The original image downloaded from the specified URL.
resized_image.png: The image resized to 256 pixels in width.
grayscale_image.png: The resized image converted to grayscale.
edged_image.png: The resized image with Canny edge detection applied.
README.md: This file, documenting the project.

Prerequisites
To run the code, you need:

Python 3.8+
A virtual environment (recommended)
The following Python packages:
opencv-python (~4.11.0)
numpy (~2.1.1)
matplotlib (~3.9.2)
requests (~2.32.3)



Setup Instructions

Clone the Repository:
git clone https://github.com/FroCode/image-processing
cd image-processing


Create and Activate a Virtual Environment:
python -m venv myenv
source myenv/bin/activate  # On Linux/Mac
myenv\Scripts\activate     # On Windows


Install Dependencies:
pip install opencv-python numpy matplotlib requests


Verify Installation:Check installed packages:
pip list



Running the Code

Execute the Script:
python main.py


Expected Output:

Console:
Prints "Hello World".
Debug messages about image download and processing.
The resized image array.


Files:
Four PNG files (original_image.png, resized_image.png, grayscale_image.png, edged_image.png) saved in the project directory.




View Results:

Open the PNG files in an image viewer to verify the outputs.
Note: If running in a headless environment, the images are saved instead of displayed due to Matplotlib's non-interactive backend.



Troubleshooting

Image Download Failure:

If the primary URL fails, the script uses a fallback URL (https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png).
Check your internet connection or try a different URL.


Image Decoding Error:

Ensure the URL points to a valid PNG/JPG file.
Reinstall OpenCV:pip uninstall opencv-python
pip install opencv-python




Matplotlib Display Issues:

If you see FigureCanvasAgg is non-interactive warnings, the script saves images to files instead of displaying them.
To enable GUI display (on a Linux desktop):sudo apt-get install python3-tk

Add matplotlib.use('TkAgg') at the top of main.py.


Alternative Environment:

If local issues persist, run the code in Google Colab for inline image display.



Assignment Submission

Files Submitted:
main.py
original_image.png
resized_image.png
grayscale_image.png
edged_image.png


Image Used: The primary image is "Das Schwarze Quadrat" from Wikimedia Commons. Due to its uniform appearance, edge detection may produce minimal output. A fallback image with more features is used if the primary URL fails.
Environment: Developed and tested on Ubuntu (HP Victus laptop) with Python 3.10 in a virtual environment.
Resources:
OpenCV Python Tutorial
Matplotlib Documentation
Requests Library
