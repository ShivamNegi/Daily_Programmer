#!/usr/bin/python3

import time
start_time = time.time()
def rev(n, digits):
    """
    Returns the reverse of the number n, which has the given number of digits.
    """
    n_str = str(n)
    rev_n = int(n_str[::-1])
    return (10 ** (digits - len(n_str))) * rev_n

def moduli(n, digits):
    """
    Returns the pair (n mod 7, rev(n) mod 7)
    """
    return (n % 7, rev(n, digits) % 7)

def inverse(val):
    """
    returns the inverse mod 7.
    """
    #        0  1  2  3  4  5  6
    return [-1, 1, 4, 5, 2, 3, 6][val]

def make_table(digits):
    """
    returns a pair of (table, modulus). table is a dictionary mapping pairs of
    (forward_modulus, backward_modulus) to pairs of (the sum of integers that
    have these moduli, number of such integers), and modulus is what to multiply
    the higher digits by when computing reverse moduli of larger numbers ending
    with these.
    """
    #if digits == 0: return ({}, -1, {})
    table = {}
    for i in range(10 ** digits):
        modulus = moduli(i, digits)
        if modulus not in table:
            table[modulus] = [0, 0]
        table[modulus][0] += i
        table[modulus][1] += 1
    return (table, inverse(10 ** digits % 7))
tables = [make_table(i) for i in range(7)]

def diff(mod_x, mod_y):
    """
    Differences of pairs of moduli
    """
    xa, xb = mod_x
    ya, yb = mod_y
    # Ensure that the results are positive even if the diff would be negative;
    # we're doing this all mod 7, so numbers should be between 0 and 6.
    return ((7 + xa - ya) % 7, (7 + xb - yb) % 7)

def mul(mod, offset):
    """
    We're trying to append to an offset-digit number with moduli mod. Return the
    desired moduli of the thing we're appending it to.
    """
    a, b = mod
    return ((7 - a) * tables[offset][1] % 7, (7 - b) % 7)

cache = {}  # Precomputed answers from partial_solutions
def partial_solutions(digits, moduli):
    """
    returns the sum of all `digits`-digit numbers whose forward/backward moduli
    are `moduli`. `digits` must be a multiple of 6. Also returns the number of
    numbers that went into this sum.
    """
    if digits == 0:
        return (0, 1)
    if digits == 6:
        return tables[6][0][moduli]
    if (digits, moduli) in cache:
        return cache[(digits, moduli)]
    result = 0
    result_count = 0
    for modulus, value_sum_pair in tables[6][0].items():
        d = diff(moduli, modulus)
        recursed = partial_solutions(digits - 6, d)
        result += (recursed[0] * 10 ** 6 * value_sum_pair[1] +
                value_sum_pair[0] * recursed[1])
        result_count += value_sum_pair[1] * recursed[1]
    cache[(digits, moduli)] = (result, result_count)
    return result, result_count

def solutions(digits):
    """
    returns the sum of all `digits`-digit numbers who are multiples of 7 both
    forwards and backwards.
    """
    if digits <= 6:
        return tables[digits][0].get((0, 0), [0, 0])[0]
    offset = digits % 6
    rest = digits - offset
    if offset == 0:
        return partial_solutions(rest, (0, 0))[0]
    result = 0
    for modulus, value_sum_pair in tables[offset][0].items():
        d = mul(modulus, offset)
        partial = partial_solutions(rest, d)
        result += (partial[0] * (10 ** offset) * value_sum_pair[1] +
                value_sum_pair[0] * partial[1])
    return result

if __name__ == "__main__":
    for i in range(1,13):
        print("{}: {}".format(i, solutions(i)))
    import sys
    sys.setrecursionlimit(5000)
    value = solutions(10000)
    #print(value)
print ("--- %s seconds ---" %(time.time() - start_time))    