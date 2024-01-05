import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_channel(ax, image, channel, color=True):
    if color:
        to_show = np.zeros_like(image)
        to_show[..., channel] = image[..., channel]
        show_image(ax, to_show, title=f"channel:{channel}")
    else:
        to_show = image[..., channel]
        show_image(ax, to_show, cmap="gray", title=f"channel:{channel}")


