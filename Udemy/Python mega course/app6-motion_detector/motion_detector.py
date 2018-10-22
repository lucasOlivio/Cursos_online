import cv2, time, pandas
import numpy as np
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
kernel = np.ones((21,21), np.uint8)

df= pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(1)

while(video.isOpened()):
    ret, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blured = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = blured
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    close = cv2.morphologyEx(thresh_delta, cv2.MORPH_CLOSE, kernel)

    (_, cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1

        (x, y ,w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (w+x,  h+y), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('close', close)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('blured frame',blured)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        if status ==1:
            times.append(datetime.now())
        break

for i in range(0, len(times), 2):
    df = df.append({"Start":times[i],"End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

cv2.destroyAllWindows
video.release()
