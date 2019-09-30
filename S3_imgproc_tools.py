import cv2
import time
import numpy as np

def invert_colors_manual(input_img):
    """Function that invert color of an image
    Args:
        input_img: an ndarray
    return an ndarray of inverted color
    """
    rows=len(input_img)
    cols=len(input_img[0])
    channels=len(input_img[0][0])
    for r in range(rows):
        for c in range(cols):
            for cha in range(channels):
                input_img[r][c][cha]=255-input_img[r][c][cha]
    return input_img

def invert_colors_numpy(input_img):
    """Function that invert color of an image using numpy
    Args:
        input_img: an ndarray
    return an ndarray of inverted color
    """
    input_img=255-input_img
    return input_img

def invert_colors_opencv(input_img):
    """Function that invert color of an image using opencv
    Args:
        input_img: an ndarray
    return an ndarray of inverted color
    """
    input_img = cv2.bitwise_not(input_img)
    return input_img


img_gray=cv2.imread("pika.png",0)#load an image in gray levels
img_bgr=cv2.imread("pika.png",1)#load an image in Blue Green Red
#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))
#display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)

start_time = time.perf_counter()
inverted = invert_colors_manual(img_bgr)
invert_colors_manual_time=(time.perf_counter() - start_time)*1000000
cv2.imshow("inverted image manual", inverted)

start_time = time.perf_counter()
inverted_np = invert_colors_numpy(img_bgr)
invert_colors_numpy_time=(time.perf_counter() - start_time)*1000000
cv2.imshow("inverted image np", inverted_np)

start_time = time.perf_counter()
inverted_ocv = invert_colors_opencv(img_bgr)
cv2.imshow("inverted image ocv",inverted_ocv)
invert_colors_ocv_time=(time.perf_counter() - start_time)*1000000

print('Time :')
print("Manual : ",invert_colors_manual_time," microsecondes")
print("Numpy : ",invert_colors_numpy_time," microsecondes")
print("CV2 : ",invert_colors_ocv_time," microsecondes")

cv2.waitKey()