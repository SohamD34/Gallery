import cv2
import numpy as np
import argparse
from utils import region_of_interest, draw_the_lines, process



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Car and Lane Detection')
    parser.add_argument('--detect', choices=['lane', 'cars'], required=True, help="Choose detection mode: 'lane' or 'cars'")
    args = parser.parse_args()

    cascade_src = 'templates/cars.xml'
    video_src = 'data/roadvidtimelapse.mp4'

    cap = cv2.VideoCapture(video_src)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    car_cascade = cv2.CascadeClassifier('templates/cars.xml')                     # Haar Cascade for car detection

    cap = cv2.VideoCapture(video_src)

    # process                                                                     # process -                 
    while cap.isOpened():
        ret, img = cap.read()
        if not ret or img is None:
            break

        if args.detect == 'lane':
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                      # Convert BGR to RGB for lane detection
            lane_img = process(rgb_img)
            lane_img_bgr = cv2.cvtColor(lane_img, cv2.COLOR_RGB2BGR)            # Convert back to BGR for imshow
            cv2.imshow('frame', lane_img_bgr)
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(gray, 1.1, 2)
            for (x, y, w, h) in cars:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.imshow('video', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.waitKey(30)

    cap.release()
    cv2.destroyAllWindows()