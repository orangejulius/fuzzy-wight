from nose.tools import *

from problem_3 import *

functions = [evaluate, evaluate2]

def _test_both(input, expected):
    for f in functions:
        assert_equal(f(input), expected)

def test_add():
    input = "1 + 1"
    _test_both(input, 2)

def test_parse():
    input = "1 + 1"
    assert_equal(parse(input), [1, '+', 1])

def test_two_adds():
    input = "1 + 1 + 2"
    _test_both(input, 4)

def test_add_multiply():
    input = "3 * 2 + 1"
    _test_both(input, 7)

def test_add_multiply2():
    input = "1 + 2 * 3"
    _test_both(input, 7)

def test_example():
    input = "5 * 6 / 3 + 1"
    _test_both(input, 11)

def test_4_operators():
    input = "1 + 2 * 3 - 4 / 5"
    _test_both(input, 6.2)

def test_power():
    input = "3 ^ 2"
    _test_both(input, 9)

def test_pow_and_sub():
    input = "2 ^ 8 - 1"
    _test_both(input, 255)

def test_pow_mult_sub():
    input = "2 ^ 8 * 4 - 1"
    _test_both(input, 1023)

def test_precedence():
    precedence_val = [1, 1, 2, 2, 3]

    for idx, operator in enumerate(operators):
        assert_equal(precedence(operator), precedence_val[idx])
