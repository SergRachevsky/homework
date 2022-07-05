#!/usr/bin/python3

import sys
from math import sqrt

RC_NOT_A_SE = -1
RC_NO_ROOTS = 0
RC_ONE_ROOT = 1
RC_TWO_ROOTS = 2

def get_input_data(args):

    # get arguments from command line (except sys.argv[0] which is a script name)
    args = args[1:]

    # convert all arguments to integers (we expect they SHOULD be integers)
    args = list(map(int, args))

    # we want number of arguments to be a multiple of three,
    # so we add zeros for missed elements
    while len(args) % 3:
        args.append(0)

    # split list of arguments to list of triads
#    triads = [args[i:i+3] for i in range(0, len(args), 3)]
    
    return [args[i:i+3] for i in range(0, len(args), 3)]


def make_se_text(a, b, c):
    # make square equation string more comfortable to read for humans
    a_str = f"{a}x^2" if abs(a) != 1 else "x^2"
    b_str = f"{' + ' if b > 0 else ' - '}{abs(b)}x" if b != 0 else ""
    c_str = f"{' + ' if c > 0 else ' - '}{abs(c)}"  if c != 0 else ""

    return f"{a_str}{b_str}{c_str} = 0"


def se_solve(a, b, c):
    
    roots = []

    # calculate discriminant of square equation
    d = b**2 - 4*a*c

    if a == 0:
        rc = -1
        text = "Not a square equation (a=0)"

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
    square_equation = make_se_text(a, b, c)
    print(f"[{a:5}, {b:5}, {c:5}]  ==>  {square_equation:24}  ==>  {text}")


if __name__ == "__main__":

    se_triads = get_input_data(sys.argv)

    for a, b, c in se_triads:

        rc, roots, text = se_solve(a, b, c)
        print_solution(a, b, c, text)
