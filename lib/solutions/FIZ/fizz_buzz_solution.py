# noinspection PyUnusedLocal
def fizz_buzz(number):
    # raise NotImplementedError()
    n = number
    if ((( n % 3 ) == 0 ) or ('3' in str(n))) \
        and ( ( n % 5 ) != 0 ) and ('5' not in str(n) ):
        return "fizz"
    elif (( n % 5 ) == 0 ) or ('5' in str(n)) \
        and (( n % 3 ) != 0 ) and ('3' not in str(n)):
        return "buzz"
    elif (( n % 3 ) == 0 ) or ('3' in str(n)) or \
       (( n % 5 ) == 0 ) or ('5' in str(n)):
        return "fizz buzz"
    else:
        return n
