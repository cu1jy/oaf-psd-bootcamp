"""
Function that returns if a given number is prime
"""
def is_prime(number: int) -> bool:
    if(number > 1):
        for x in range(2, number):
            if(number % x == 0):
                return False
        return True
    return False
