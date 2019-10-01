import pytest
import cv2
import S3_imgproc_tools as s3
import numpy as np

"""-------------TEST invert_colors_manual---------------"""
def test_invert_colors_manual_working():
    img_bgr=cv2.imread("pika.png",1)
    inverted = s3.invert_colors_manual(img_bgr)
    assert type(inverted)==np.ndarray

"""-------------TEST invert_colors_numpy---------------"""
def test_invert_colors_numpy_working():
    img_bgr=cv2.imread("pika.png",1)
    inverted = s3.invert_colors_numpy(img_bgr)
    assert type(inverted)==np.ndarray

"""-------------TEST invert_colors_opencv---------------"""
def test_invert_colors_opencv_working():
    img_bgr=cv2.imread("pika.png",1)
    inverted = s3.invert_colors_opencv(img_bgr)
    assert type(inverted)==np.ndarray