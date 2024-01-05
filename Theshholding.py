import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_red(image):
    img1 = cv2.imread(image, cv2.IMREAD_COLOR)

    h, s, v = cv2.split(img1)

    hsv_image = cv2.merge([h, s, v])

    out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    red_color_low = (70,50,60)
    red_color_high = (250,255,255)
    only_red_hsv = cv2.inRange(out, red_color_low, red_color_high)

