

# TDD - Test Driven Development
# RED - GREEN - REFACTOR
# 1 - Write Unit-Test first and then Develop
# 2 - Write only enough test to fail
# 3 - Write only enough to pass the pass


# FizzBuzz - Takes a number fizzbuzz(num)
# Fizz    - If the number is a multiple of 3
# Buzz    - If the number is a multiple of 5
# FizzBuzz - If the number is multiple of 3 & 5

# unit under development
import sys
sys.path.append('./src')

from m_fizzbuzz import fizzbuzz


# unit-test if there is fizzbuzz(num)

def test_fizzbuzz_zero_args():
    assert fizzbuzz() == None


def test_fizzbuzz_str_input():
    assert fizzbuzz('test string') == None


def test_fizzbuzz_bool_input():
    assert fizzbuzz(True) == None
    assert fizzbuzz(False) == None


def test_fizzbuzz_numeric_str_input():
    assert fizzbuzz('35') == 'buzz'


def test_fizzbuzz_multiple_3_fizz():
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(18) == 'fizz'
    assert fizzbuzz(-21) == 'fizz'


def test_fizzbuzz_multiple_5_buzz():
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(20) == 'buzz'
    assert fizzbuzz(-35) == 'buzz'


def test_fizzbuzz_multiple_3_5():
    assert fizzbuzz(15) == 'fizzbuzz'
    assert fizzbuzz(-60) == 'fizzbuzz'


def test_fizzbuzz_floats():
    assert fizzbuzz(6.0) == 'fizz'
    assert fizzbuzz(25.0) == 'buzz'
    assert fizzbuzz(30.0) == 'fizzbuzz'


def test_fizzbuzz_negatives():
    assert fizzbuzz(7) == 7
    assert fizzbuzz(97) == 97
    assert fizzbuzz(-2) == -2
    assert fizzbuzz(4.0) == 4.0
    assert fizzbuzz(9.01) == 9.01
