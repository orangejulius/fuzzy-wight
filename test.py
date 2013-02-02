from nose.tools import *

from problem_3 import *

def test_add():
    input = "1 + 1"
    assert_equal(evaluate(input), 2)

def test_parse():
    input = "1 + 1"
    assert_equal(parse(input), [1, '+', 1])

def test_two_adds():
    input = "1 + 1 + 2"
    assert_equal(evaluate(input), 4)

def test_add_multiply():
    input = "3 x 2 + 1"
    assert_equal(evaluate(input), 7)

def test_add_multiply2():
    input = "1 + 2 x 3"
    assert_equal(evaluate(input), 7)

def test_example():
    input = "5 x 6 / 3 + 1"
    assert_equal(evaluate(input), 11)

def test_precedence():
    operators = [ '+', '-', 'x', '/' ]
    precedence_val = [1, 1, 2, 2]

    for idx, operator in enumerate(operators):
        assert_equal(precedence(operator), precedence_val[idx])
