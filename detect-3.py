import os, cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-f', '--file', help = 'file path')
ap.add_argument('-r', '--rotate', default = False, type=bool, help = 'flag for rotating the frames')
ap.add_argument('-g', '--gray', default = False, type=bool, help = 'flag for converting the frames to grayscale')
ap.add_argument('-s', '--save', default = False, type=bool, help = 'flag for saving the frames')
args = vars(ap.parse_args())

for i in os.listdir(args['file']):
    i = os.path.join(args['file'],i)
    cap = cv2.VideoCapture(i)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (w,h)

    while True:
        ret, frame = cap.read()
        if args['gray']:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (int(frame.shape[1]*.2), int(frame.shape[0]*.2)))
        if args['rotate']:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        if args['save']:
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            out = cv2.VideoWriter(str(i) + '_rotated_output.avi', fourcc, 20.0, size)
            out.write(frame)
            out.release()
    cap.release()
cv2.destroyAllWindows()
