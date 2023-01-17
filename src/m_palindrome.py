'''Unit Under Development: is_palindrome(p_str)

'''


def is_palindrome(p_str=''):
    '''Unit Under Development: is_palindrome(p-str)

    This is the unit under development to be tested
    '''

    if not isinstance(p_str, str)
        return None

    if len(p_str) == 0:
        return None

    if len(p_str) == 1:
        return True

    p_str = p_str.lower()
    p_run = len(p_str)//2

    for char_index in range(0, p_run):

        if p_str[char_index] != p_str[len(p_str)-char_index-1]:
            return False

    return True
