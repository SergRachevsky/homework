#!/usr/bin/python3
#
# This script solves a regular quadratic equation (a*x^2 + b*x + c = 0).
# The program receives parameters of the equation as a stream of numbers from the command line:
#
# > se_solver 3 4 5 0 4 -4 11 22 123 45 42 42 67 1001 …
#
# All number are integers and some of them can be 0. 
#
# As result the script prints input numbers, textual representation of the equation and solution for the equation, 
# one line per equation.
#
# There are also unit tests for this script located in test_se_solver.py. 
# Description of how to run these tests and how to interpret test results could be found in README.md.
#
# About variables naming: 
# In the script I use 'a', 'b' and 'c' variables as coefficients of quadratic equation and
# x, x1, x2 as roots of quadratic equation

import sys
from math import sqrt

RC_NOT_A_SE = -1
RC_NO_ROOTS = 0
RC_ONE_ROOT = 1
RC_TWO_ROOTS = 2

def get_input_data(args):
    """ 
    Makes triads (a, b, and c coefficients) from input numbers.

    Args:
        args (string): space separated integers

    Returns:
        list: list of lists of input numbers grouped by three
    """
    # get arguments from command line (except sys.argv[0] which is a script name)
    args = args[1:]

    # convert all arguments to integers (we expect they SHOULD be integers)
    args = list(map(int, args))

    # we want number of arguments to be a multiple of three,
    # so we add zeros for missed elements
    while len(args) % 3:
        args.append(0)

    # return value is list of lists of input numbers grouped by three
    return [args[i:i+3] for i in range(0, len(args), 3)]

def se_solve(a, b, c):
    """
    Solves regular quadratic equation.

    Args:
        a (integer): coefficient a
        b (integer): coefficient b
        c (integer): coefficient c

    Returns:
        tuple: tuple of return code (integer), roots (list) and textual representation of solution (string)
    """
    # here we actually solve regular quadratic equation and also make textual representation of solution
    # 
    # result is tuple of:
    #  - return code constant
    #  - list of roots (empty for no roots and consist one of two numbers if equations has root(s))
    #  - textual representation of solution used later for printing out
    #
    # note: rc variable isn't used in se_solver.py but it is used in test_se_solver.py

    roots = []

    # calculate discriminant of square equation
    d = b**2 - 4*a*c

    # regular quadratic equation should have (a <> 0) so we make check for this
    if a == 0:
        rc = -1
        text = "Not a square equation (a=0)"

    # equation has two roots if discriminant is positive number, has one root if discriminant is equal to zero and
    # has no roots if discriminant is negative number
    elif d > 0:
        rc = 2
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        text = f"x1 = {x1:6.2f}; x2 = {x2:6.2f}"
        roots.append(x1)
        roots.append(x2)

    elif d == 0:
        rc = 1
        x = -b / (2 * a)
        text = f"x  = {x:6.2f}"
        roots.append(x)
    else:
        rc = 0
        text = "No roots"

    return rc, roots, text

def print_solution(a, b, c, text):
    """
    Prints quadratic equation and its soulution

    Args:
        a (integer): coefficient a
        b (integer): coefficient b
        c (integer): coefficient c
        text (string): textual representation of solution
    Returns:
        None
    """
    square_equation = make_se_text(a, b, c)
    print(f"[{a:5}, {b:5}, {c:5}]  ==>  {square_equation:24}  ==>  {text}")

def make_se_text(a, b, c):
    """
    Makes square equation string from a, b, c coefficients.

    Args:
        a (integer): coefficient a
        b (integer): coefficient b
        c (integer): coefficient c

    Returns:
        string: textual representation of square equation
    """
    # make square equation string more comfortable to read for humans
    # (remove equation elements with coefficient equal to zero and also 
    # correctly put minuses and pluses into the result string) 
    a_str = f"{a}x^2" if abs(a) != 1 else "x^2"
    b_str = f"{' + ' if b > 0 else ' - '}{abs(b)}x" if b != 0 else ""
    c_str = f"{' + ' if c > 0 else ' - '}{abs(c)}"  if c != 0 else ""

    return f"{a_str}{b_str}{c_str} = 0"

if __name__ == "__main__":
    # very simple logic: get triads of coefficients, 
    # then solve equation and print result for every triad in a loop

    se_triads = get_input_data(sys.argv)

    for a, b, c in se_triads:
        rc, roots, text = se_solve(a, b, c)
        print_solution(a, b, c, text)
