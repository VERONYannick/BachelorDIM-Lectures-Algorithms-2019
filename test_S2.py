import pytest
import numpy as np
import cv2
import S1_algotools as s1

"""-------------TEST average_above_zero---------------"""
def test_average_above_zero_expected_list():
    """Function that test if average_above_zero raise exeption when the param is not a list"""
    with pytest.raises(ValueError):
        s1.average_above_zero(15)

def test_average_above_zero_empty():
    """Function that test if average_above_zero raise exeption when the param is an empty list"""
    with pytest.raises(ValueError):
        s1.average_above_zero([])

def  test_average_above_zero_expected_number_list():
    """Function that test if average_above_zero raise exeption when the param is an not a numbers list"""
    with pytest.raises(ValueError):
        s1.average_above_zero(["e","r","r","o","r"])

def test_average_above_zero_working():
    """Function that test if average_above_zero return the correct average"""
    assert s1.average_above_zero([10,20])==15.0



"""--------------TEST max_value-----------------------"""
def test_max_value_expected_list():
    """Function that test if max_value raise exeption when the param is not a list"""
    with pytest.raises(ValueError):
        s1.max_value(15)

def test_max_value_empty():
    """Function that test if max_value raise exeption when the param is an empty list"""
    with pytest.raises(ValueError):
        s1.max_value([])

def  test_max_value_expected_number_list():
    """Function that test if max_value raise exeption when the param is an not a numbers list"""
    with pytest.raises(ValueError):
        s1.max_value(["e","r","r","o","r"])

def test_max_value_working():
    """Function that test if max_value return the max value and index"""
    assert s1.max_value([10,51,48,63,24])==(63,3)



"""--------------TEST reverse_table-------------------"""
def test_reverse_table_expected_list():
    """Function that test if reverse_table raise exeption when the param is not a list"""
    with pytest.raises(ValueError):
        s1.reverse_table(15)

def test_reverse_table_empty():
    """Function that test if reverse_table raise exeption when the param is an empty list"""
    with pytest.raises(ValueError):
        s1.reverse_table([])

def  test_reverse_table_expected_number_list():
    """Function that test if reverse_table raise exeption when the param is an not a numbers list"""
    with pytest.raises(ValueError):
        s1.reverse_table(["e","r","r","o","r"])

def test_revese_table_working():
    """Function that test if reverse_table return the reversed array"""
    assert np.array_equal(s1.reverse_table([10,15,20,12,15]),[15,12,20,15,10])==True


"""--------------TEST --------------------------"""
def test_roi_bbox_expected_ndarray():
    """Function that test if reverse_table raise exeption when the param is not a ndarray"""
    with pytest.raises(ValueError):
        s1.reverse_table(15)

def test_roi_bbox_empty():
    """Function that test if reverse_table raise exeption when the param is an empty list"""
    with pytest.raises(ValueError):
        s1.reverse_table([])

def test_roi_bbox_working():
    img=cv2.imread("img_sample.png",0)
    assert s1.roi_bbox(img)


"""--------------TEST random_fill_sparse---------------"""
def test_random_fill_sparse_working():
    """Function that test if random_fill_sparse return an array with 'X'"""
    charar=np.chararray((5, 5))
    charar[:] = '0'
    arr = s1.random_fill_sparse(charar,2)
    condition = arr == b'X'
    assert np.count_nonzero(condition)==2
