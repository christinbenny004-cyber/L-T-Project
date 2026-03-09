# Building Surface Damage Analysis using OpenCV

## Project Overview

Municipal engineers perform regular safety audits to identify structural damages such as cracks in buildings. Manual inspection can be time-consuming and may fail to detect small cracks.

This project uses **OpenCV image processing techniques** to automatically detect cracks in building surface images, calculate **defect density**, and classify the damage level as **Minor, Moderate, or Major**.

---

## Project Objectives

* Detect cracks in wall or masonry images using **OpenCV segmentation techniques**.
* Analyze multiple images and calculate **defect density**.
* Classify structural damage based on crack density.
* Assist engineers in identifying potentially unsafe building structures.

---

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib

---

## Methodology

1. **Image Acquisition**
   Building surface images are collected from publicly available sources.

2. **Preprocessing**

   * Convert image to grayscale
   * Apply Gaussian Blur to reduce noise

3. **Segmentation**

   * Thresholding to separate crack pixels
   * Canny edge detection to highlight crack edges

4. **Crack Detection**
   Morphological operations are applied to improve crack visibility.

5. **Defect Density Calculation**

   Defect Density = Crack Pixels / Total Pixels

6. **Damage Classification**

| Defect Density | Damage Level    |
| -------------- | --------------- |
| < 0.01         | Minor Damage    |
| 0.01 – 0.03    | Moderate Damage |
| > 0.03         | Major Damage    |

---

## Project Structure

```
Building-Surface-Damage-Analysis
│
├── crack_analysis.py
├── README.md
│
├── images
│   ├── wall1.jpg
│   ├── wall2.jpg
│   └── wall3.jpg
│
└── results
    ├── output1.png
    └── output2.png
```

---

## Installation

Install required libraries:

```
pip install opencv-python numpy matplotlib
```

---


## Sample Output

```
Image: wall1.jpg
Defect Density: 0.008
Damage Level: Minor

Image: wall2.jpg
Defect Density: 0.019
Damage Level: Moderate
```

The system displays the detected crack regions and prints the damage classification.

---

## Applications

* Structural health monitoring
* Smart city infrastructure inspection
* Building safety audits
* Bridge and concrete surface monitoring

---

## Limitations

* Lighting conditions may affect crack detection accuracy.
* Surface texture may sometimes produce false edges.
* Works best with clear wall images.

---

## Future Improvements

* Use **deep learning models (CNN)** for higher accuracy.
* Implement **real-time crack detection systems**.
* Integrate with **drone-based inspection** for large buildings.
* Develop a **GUI application for engineers**.

---

## License

This project is developed for **academic purposes** as part of a coursework assignment.
