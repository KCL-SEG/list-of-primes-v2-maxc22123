"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError
    else:
        lst = [2]
        p = 3
        while len(lst) < number_of_primes:
            for i in range(2,p):
                if p % i == 0:
                    p += 1
                    break
            else:
                lst.append(p)
                p += 1


    return lst
