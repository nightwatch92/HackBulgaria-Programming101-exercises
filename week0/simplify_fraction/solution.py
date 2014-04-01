# 0.29.simplify_fractions.py
from fractions import *
def simplify_fraction(fraction1):
    # b = Fraction(fraction1[0], fraction1[1])
    # output Fraction(ala-bala).

    gr_common_div = gcd(fraction1[0], fraction1[1])
    numerator = fraction1[0] // gr_common_div
    denominator = fraction1[1] // gr_common_div
    return (numerator, denominator)

# def main():
#     print(simplify_fraction((3,9)))
#     print(simplify_fraction((1,7)))
#     print(simplify_fraction((1,7)))
#     print(simplify_fraction((1,7)))
#     print(simplify_fraction((4,10)))
#     print(simplify_fraction((63,462)))

# if __name__ == '__main__':
#     main()