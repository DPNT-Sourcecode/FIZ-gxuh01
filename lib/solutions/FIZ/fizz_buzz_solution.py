# noinspection PyUnusedLocal
def fizz_buzz(number):
    # raise NotImplementedError()
    n = number
    c_fizz = (( n % 3 ) == 0 ) or ('3' in str(n))
    c_buzz = (( n % 5 ) == 0 ) or ('5' in str(n))
    if c_fizz and c_buzz:
        return "fizz buzz"
    elif c_fizz:
        return "fizz"
    elif c_buzz:
        return "buzz"
    else:
        return n