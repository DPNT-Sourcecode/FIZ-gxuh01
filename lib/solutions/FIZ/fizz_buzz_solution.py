# noinspection PyUnusedLocal
def fizz_buzz(number):
    # raise NotImplementedError()
    n = number
    # c_deluxe = ( len(set(str(n))) == 1 ) and ( n > 10 ) and ( n % 2 == 0)
    # c_fake_deluxe = ( len(set(str(n))) == 1 ) and ( n > 10 ) and ( n % 2 != 0)
    c3 = (( n % 3 ) == 0 ) and ('3' in str(n))
    c5 = (( n % 5 ) == 0 ) and ('5' in str(n))
    c_deluxe =  ( c3 or c5 ) and ( n % 2 == 0)
    c_fake_deluxe = ( c3 or c5 ) and ( n % 2 != 0)
    c_fizz = (( n % 3 ) == 0 ) or ('3' in str(n))
    c_buzz = (( n % 5 ) == 0 ) or ('5' in str(n))
    if c_fizz and c_buzz and c_deluxe:
        return "fizz buzz deluxe"
    elif c_fizz and c_buzz and c_fake_deluxe:
        return "fizz buzz fake deluxe"
    elif c_fizz and c_buzz:
        return "fizz buzz"
    elif c_fizz and c_deluxe:
        return "fizz deluxe"
    elif c_buzz and c_deluxe:
        return "buzz deluxe"
    elif c_fizz and c_fake_deluxe:
        return "fizz fake deluxe"
    elif c_buzz and c_fake_deluxe:
        return "buzz fake deluxe"
    elif c_fizz:
        return "fizz"
    elif c_buzz:
        return "buzz"
    elif c_deluxe:
        return "deluxe"
    elif c_fake_deluxe:
        return "fake deluxe"
    else:
        return n