# homework
This script solves a regular quadratic equation. 
The program receives parameters of the equation as a stream of numbers from the command line:

```
> se_solver 3 4 5 0 4 -4 11 22 123 45 42 42 67 1001 …
```

All number are integers and some of them can be 0. 

As result the script prints input numbers, textual representation of the equation and solution for the equation, 
one line per equation.

Here is an example of script's output:

```
$ python3 se_solver.py 1 2 -3 4 5 6 9 -6 10 78 14 0 0 -4 12 -9
[    1,     2,    -3]  ==>  x^2 + 2x - 3 = 0          ==>  x1 =   1.00; x2 =  -3.00
[    4,     5,     6]  ==>  4x^2 + 5x + 6 = 0         ==>  No roots
[    9,    -6,    10]  ==>  9x^2 - 6x + 10 = 0        ==>  No roots
[   78,    14,     0]  ==>  78x^2 + 14x = 0           ==>  x1 =   0.00; x2 =  -0.18
[    0,    -4,    12]  ==>  0x^2 - 4x + 12 = 0        ==>  Not a square equation (a=0)
[   -9,     0,     0]  ==>  -9x^2 = 0                 ==>  x  =  -0.00
```

There are also unit tests for this script located in test_se_solver.py. Tests are based on ```unittest``` Pyton module.

Below are some examples how to use tests.

1. Fastest and simpliest way to get info that all tests are passed:
```
$ python3 -m unittest discover
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```
You will see only summary of tests.

2. If you want to see more information about which tests present, use ```'-v'``` key:

```
$ python3 -m unittest discover -v
test_get_input_data (test_se_solver.TestSeSolver)
Make sure arguments from command line are converted into the list of triads correctly ... ok
test_get_input_data_empty (test_se_solver.TestSeSolver)
No arguments should lead to empty list of triads ... ok
test_make_se_text (test_se_solver.TestSeSolver)
check if we can costruct the equation text correctly using different variants of arguments ... ok
test_no_roots (test_se_solver.TestSeSolver)
Check that we correctly solved the equation with no roots ... ok
test_not_a_se (test_se_solver.TestSeSolver)
If the first of the three is zero then result should be RC_NOT_A_SE ... ok
test_one_root (test_se_solver.TestSeSolver)
Check that we correctly solved the equation with one root ... ok
test_two_roots (test_se_solver.TestSeSolver)
Check that we correctly solved the equation with two roots ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
In this case you will see name of every test with its result.

3. Also you may run only specific test with next command:

```
$ python3 -m unittest test_se_solver.TestSeSolver.test_not_a_se -v 
test_not_a_se (test_se_solver.TestSeSolver)
If the first of the three is zero then result should be RC_NOT_A_SE ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
Here we got results concerning 'test_not_a_se' test only.

# Tests results interpretation

If test has passed, you will see 'ok' after every test name and also "OK" as a last line of output.
Like it was in examples above.

If test has failed you will see "FAIL' after every failed test name:

```
If the first of the three is zero then result should be RC_NOT_A_SE ... FAIL
```

Also you will see traceback with the line caused error:

```
======================================================================
FAIL: test_not_a_se (test_se_solver.TestSeSolver)
If the first of the three is zero then result should be RC_NOT_A_SE
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/serg/Work/homework/test_se_solver.py", line 32, in test_not_a_se
    self.assertEqual(se_solve(1, 4, 5)[0], RC_NOT_A_SE, "Should be -1")
AssertionError: 0 != -1 : Should be -1

----------------------------------------------------------------------
```
Pay attention to text of AssertionError, it can be useful to understand why test has been failed.

And finally you will see summary of testing with number of failed tests:

```
Ran 1 test in 0.000s
FAILED (failures=1)
```
