def fizzbuzz(num=None):

    if num == None:
        return None

    elif isinstance(num, str):
        try:
            num = int(num)

        except ValueError:
            return None

    elif isinstance(num, bool):
        return None

    if (num % 3) == 0:
        if (num % 5) == 0:
            return 'fizzbuzz'
        return 'fizz'
    elif (num % 5) == 0:
        return 'buzz'

    return num


fizzbuzz(12, 34, 45, 60, 90)