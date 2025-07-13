# NumPy - RGB Histogram

## RGB Histogram Image Analyzer

A Python tool that analyzes an existing image and generates histograms showing the number of pixels for each RGB value (0–255) per color channel.

![Image Example](Task_numpy-Shira_Taieb/img_color.png)  
![Histogram Example](Task_numpy-Shira_Taieb/histogram_color.png)

## Description

The tool scans an image that already exists in the code folder (e.g., `black.png`, `color.png`) and computes the distribution of pixel values for each of the three color channels:

- **X-axis** – Color intensity values (0–255)
- **Y-axis** – Number of pixels with that color value

For example, how many pixels have a red value of 50, or a green value of 130, and so on.

## How to Run

1. Make sure Python 3 is installed on your system.
2. Install the required libraries:
   pip install -r requirements.txt
3. Run the script:
   python program.py

## How to Run with Docker

To run the project using Docker, follow these steps:

1. Make sure you have Docker installed on your computer.
2. Build the Docker image:
   docker build -t <IMAGE_NAME>
3. Run the Docker container:
   docker run -it --rm -v ${PWD}:/app <IMAGE_NAME>
   remark:
   Because Docker does not support displaying graphs, an image will be created in your project folder that contains the appearance of the created graph, and you will also receive a success message in the terminal.
