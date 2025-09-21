import cv2
import numpy as np
import argparse


def region_of_interest(img, vertices):
    '''
    Define a region of interest (ROI) in the image.
    Args:
        img (numpy.ndarray): The input image.
        vertices (numpy.ndarray): The vertices defining the polygonal region of interest.
    
    Returns:
        numpy.ndarray: The masked image where only the region of interest is visible.
    '''
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)                                  # Fill the polygon defined by vertices with white color
    masked_image = cv2.bitwise_and(img, mask)                                       # Apply the mask to the image      
    return masked_image


def drow_the_lines(img, lines):
    '''
    Draw the detected lines on the image.
    Args:
        img (numpy.ndarray): The original image.
        lines (numpy.ndarray): The detected lines in the format [[[x1, y1, x2, y2], ...]].
    
    Returns:
        numpy.ndarray: The image with the detected lines drawn on it.
    '''
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=5)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)                            # Blend the original image with the lines
    return img



def process(image):
    '''
    Process the image to detect lane lines. 
    Steps:
        1. Convert the image to grayscale.
        2. Apply Canny edge detection.
        3. Define a region of interest (ROI) to focus on the lane area.
        4. Use Hough Transform to detect lines in the ROI.
        5. Draw the detected lines on the original image.

    Args:
        image (numpy.ndarray): The input image in RGB format.
    Returns:
        numpy.ndarray: The image with detected lane lines drawn on it.
    '''

    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (2, height),
        (width/2.18, height/1.48),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)                                                        # Convert RGB to Grayscale 
    canny_image = cv2.Canny(gray_image, 100, 120)                                                               # Apply Canny edge detection     
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32),)         # Crop the image to the region of interest

    lines = cv2.HoughLinesP(cropped_image,                                      
                rho=2,                                          # rho - distance resolution in pixels                       
                theta=np.pi/180,                                # theta - angle resolution in radians
                threshold=50,                                   # threshold - minimum number of votes to consider a line 
                lines=np.array([]),                             # lines - output array to store the detected lines  
                minLineLength=40,
                maxLineGap=100
            )                                                   # Detect lines using Hough Transform
    image_with_lines = drow_the_lines(image, lines)                 
    return image_with_lines

