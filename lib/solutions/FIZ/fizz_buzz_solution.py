# noinspection PyUnusedLocal
def fizz_buzz(number):
    # raise NotImplementedError()
    n = number
    if (( n % 3 ) == 0 ) and (( n % 5 ) == 0 ):
        return "fizz buzz"
    elif (( n % 3 ) == 0 ):
        return "fizz"
    elif (( n % 5 ) == 0 ):
        return "buzz"
    else:
        return n
