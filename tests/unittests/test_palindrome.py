''' Test Set: test_whitebox

Unit Under Development: is_palindrome(p-str)

Unit-Test(s):
1. test_int_is_palindrome
2. test_float_is_palindrome
3. test_bool_is_palindrome
4. test_no_args_is_palindrome
5. test_empty_str_is_palindrome
6. test_single_char_is_palindrome
7. test_positives_mix_case_is_palindrome
8. test_positives_same_case_is_palindrome
9. test_negatives_is_palindrome

'''

from m_palindrome import is_palindrome
import sys
sys.path.append('./src')


# *TDD - Test Driven Development (heart of eXtreme Programming XP)
# *TDD Cycle: RED -> GREEN -> REFACTOR -> RED -> GREEN -> REFACTOR -> ...
# *TDD Principles (Heart of Unit-Testing):
# * 1. Unit Test is developed before the actual Unit itself.
# * 2. Writing just enough or minimum unit-test to fail
# * 3. Writing just enough or minimum unit to pass


# unit-test
def test_int_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_int_is_palindrome()

    This unit-test will test integer argument
    '''
    assert is_palindrome(1) is None


def test_float_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test float argument
    '''
    assert is_palindrome(23.67) is None


def test_bool_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test boolean argument
    '''
    assert is_palindrome(True) is None


def test_no_args_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test zero arguments
    '''
    assert is_palindrome() is None


def test_empty_str_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test empty string argument
    '''
    assert is_palindrome('') is None


def test_single_char_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test single character string argument
    '''
    assert is_palindrome('b') is True


# todo: asking for alphanumeric

def test_positives_mix_case_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test regular positive mixcases i.e. return True
    '''

    assert is_palindrome('Rotator') is True
    assert is_palindrome('deifieD') is True


def test_positives_same_case_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test regular positive cases i.e. return True
    '''
    assert is_palindrome('abccba') is True
    assert is_palindrome('racecar') is True
    assert is_palindrome('aibohphobia') is True
    assert is_palindrome('ratstar') is True
    assert is_palindrome('madamimadam') is True
    assert is_palindrome('123454321') is True


def test_negatives_mix_case_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test regular negative cases i.e. return False
    '''

    assert is_palindrome('LEVal') is False


def test_negatives_same_case_is_palindrome():
    '''Unit-Test: Testing is_palindrome(p_str) return values

    Unit:      is_palindrome(p_str)
    Unit-Test: test_is_palindrome()

    This unit-test will test regular negative cases i.e. return False
    '''
    assert is_palindrome('abcxba') is False
    assert is_palindrome('zebrbarbez') is False
    assert is_palindrome('1234564321') is False
