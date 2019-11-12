# noinspection PyUnusedLocal
def fizz_buzz(number):
    # raise NotImplementedError()
    n = number
    if (( n % 3 ) == 0 ) or ('3' in str(n)) or \
       (( n % 5 ) == 0 ) or ('5' in str(n)):
        return "fizz buzz"
    elif (( n % 3 ) == 0 ) or ('3' in str(n)):
        return "fizz"
    elif (( n % 5 ) == 0 ) or ('5' in str(n)):
        return "buzz"
    else:
        return n
