# Car and Lane Detection in Videos

This project implements real-time car and lane detection in videos using OpenCV. It provides two detection modes:
- **Lane Detection**: Uses Canny edge detection and Hough Transform to identify lane lines
- **Car Detection**: Uses Haar cascade classifiers to detect vehicles


## Installation

1. Clone the repository:
```bash
git clone https://github.com/SohamD34/Car-Lane-Detection.git
cd Car-Lane-Detection
```

2. Install required dependencies:
```bash
pip install opencv-python numpy
```

## Usage

The script supports two detection modes that can be selected via command-line arguments:

### Lane Detection
```bash
python detect.py --detect lane
```

### Car Detection
```bash
python detect.py --detect cars
```

## File Structure

```
Car-Lane-Detection/
├── detect.py              # Main detection script
├── utils.py               # Utility functions for processing video frames
├── README.md              # Project documentation
├── data/
│   └── roadvidtimelapse.mp4   # Sample video file
└── templates/
    └── cars.xml           # Haar cascade classifier for car detection
```

## Sample Output

The application will display:
- **Lane Detection Mode**: Original video with green overlay lines marking detected lanes
- **Car Detection Mode**: Original video with yellow bounding boxes around detected vehicles
