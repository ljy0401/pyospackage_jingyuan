"""
A test module that tests your calculate module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the calculate.py
module.
"""

from pyospackage_jingyuan.calculate import add_num, multiply_num

def test_add_num():
    """
    Test that add_num works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_num(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"
    
def test_multiply_num():
    """
    Test that multiply_num works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = multiply_num(4, 2)
    expected_out = 8
    assert  out == expected_out, f"Expected {expected_out} but got {out}"
