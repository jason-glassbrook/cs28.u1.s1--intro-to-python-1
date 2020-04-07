############################################################
# is_prime (STRETCH)
############################################################


import sys
import math


############################################################


def is_integer(n):

    if isinstance(n, int):
        return True

    elif isinstance(n, float):
        return n.is_integer()

    else:
        return False


def is_prime(n):

    for f in range(2, int(math.sqrt(n)) + 1):
        if n % f == 0:
            return False

    return True

############################################################
# MAIN
############################################################


for arg in sys.argv:

    print()

    # guard for only numbers
    try:

        n = float(arg)

    except:

        print(f'"{arg}" is not a number.')
        continue

    # guard for only integers
    if is_integer(n):

        if is_prime(int(n)):

            print(f'{arg} is prime.')

        else:

            print(f'{arg} is not prime.')

    else:

        print(f'{arg} is not an integer.')
