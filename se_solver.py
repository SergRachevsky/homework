#!/usr/bin/python3

import sys
from math import sqrt

def get_input_data(args):

    # get arguments from command line (except sys.argv[0] which is a script name)
    args = args[1:]

    # convert all arguments to integers (we expect they SHOULD be integers)
    args = list(map(int, args))

    # split list of arguments to list of triads
    return [args[i:i+3] for i in range(0, len(args), 3)]


def make_sqare_equation(a, b, c):
    # make square equation string more comfortable to read for humans
    a_str = f"{a}x^2" if abs(a) != 1 else "x^2"
    b_str = f"{' + ' if b > 0 else ' - '}{abs(b)}x" if b != 0 else ""
    c_str = f"{' + ' if c > 0 else ' - '}{abs(c)}"  if c != 0 else ""

    return f"{a_str}{b_str}{c_str} = 0"

def make_text_solution(solution):
    print(solution)
    exit()
    ...

def se_solve(a, b, c):
    
    solution = []
    # calculate discriminant of suare equation
    d = b**2 - 4*a*c

    if a == 0:
#        result = "Not a square equation (a = 0)"
        solution.append(-1)

    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
#        result = f"x1 = {x1:6.2f}; x2 = {x2:6.2f}"
        solution = (2, x1, x2)

    elif d == 0:
        x = -b / (2 * a)
#        result = f"x  = {x:6.2f}"
        solution.append(1, x)

    else: 
#        result = "No roots"
        solution.append(0)

    return solution


def print_solution(a, b, c, roots):

    square_equation = make_sqare_equation(a, b, c)
    text_solution = make_text_solution(roots)

#    se_triad_str = f"[{', '.join([f'{i:4}' for i in se_triad])}]"
#    print(f"{se_triad_str:15}  ==>  {square_equation:24}  ==>  {roots}")
    print(f"[{a:5}, {b:5}, {c:5}]  ==>  {square_equation:24}  ==>  {text_solution}")


    ...


if __name__ == "__main__":
    se_triads = get_input_data(sys.argv)

    for se_triad in se_triads:

        a = se_triad[0]
        b = se_triad[1] if len(se_triad) > 1 else 0
        c = se_triad[2] if len(se_triad) > 2 else 0

        solution = se_solve(a, b, c)
        print_solution(a, b, c, solution)
