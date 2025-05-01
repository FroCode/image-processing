# Image Processing Assignment

This repository contains the solution for **Task #1 - Basics of Image Processing**.

## 🧾 Overview

The project demonstrates fundamental operations in image processing using Python:

- Load and display a local image (simulated via download).
- Load an image from a remote URL (Wikimedia Commons).
- Resize the image to a width of 256 pixels.
- Print the resized image array.
- Optionally convert the image to grayscale.
- Optionally apply Canny edge detection.

## 📂 Files

| File Name              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| `main.py`              | Main script implementing the processing steps.               |
| `original_image.png`   | Original image downloaded from the URL.                      |
| `resized_image.png`    | Image resized to 256px width.                                |
| `grayscale_image.png`  | Grayscale version of the resized image.                      |
| `edged_image.png`      | Result of applying Canny edge detection to the resized image.|
| `README.md`            | This documentation file.                                     |
| `requirements.txt`     | List of required Python packages.                            |

## ✅ Prerequisites

- Python 3.8+
- A virtual environment (recommended)
- Required packages:
  - `opencv-python==4.11.0.0`
  - `numpy==2.1.1`
  - `matplotlib==3.9.2`
  - `requests==2.32.3`

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/FroCode/image-processing
cd image-processing
pip install -r requirements.txt
python main.py

