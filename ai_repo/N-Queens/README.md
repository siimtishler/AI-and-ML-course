The code successfully completes the N Queens problem
The max N value I tested with was 100, because I did not have
the patience to try with larger N values.

For smaller N puzzles the boards will be shown in the output:

    The output for N = 4
    Initial pos conflicts: 4

    BOARD:
    [' ', 'Q', ' ', ' ']
    [' ', ' ', 'Q', ' ']
    [' ', ' ', ' ', 'Q']
    ['Q', ' ', ' ', ' ']

    VECTOR before: [3, 0, 1, 2]
    Found in 4 iterations, 0.00 seconds

    BOARD:
    [' ', 'Q', ' ', ' ']
    [' ', ' ', ' ', 'Q']
    ['Q', ' ', ' ', ' ']
    [' ', ' ', 'Q', ' ']

    VECTOR after: [2, 0, 3, 1]

    N: 4
    Avg time:0.00s
    Restart val: 16

    The output for N = 8
    Initial pos conflicts: 8

    BOARD:
    [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ']
    [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ']
    ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ']
    [' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q']
    [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ']

    VECTOR before: [3, 5, 1, 0, 2, 4, 7, 6]
    Found in 633 iterations, 0.01 seconds

    BOARD:
    [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ']
    [' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q']
    [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ']
    ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ']

    VECTOR after: [6, 1, 5, 2, 0, 3, 7, 4]

    N: 8
    Avg time:0.01s
    Restart val: 64

    The output for N = 15
    Initial pos conflicts: 5

    BOARD:
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ']
    [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ']

    VECTOR before: [3, 8, 13, 4, 9, 1, 2, 7, 10, 14, 11, 0, 12, 6, 5]
    Found in 783 iterations, 0.02 seconds

    BOARD:
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ']
    [' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ']
    [' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    VECTOR after: [9, 13, 6, 1, 14, 5, 11, 8, 4, 12, 3, 0, 7, 10, 2]

    N: 15
    Avg time:0.02s
    Restart val: 225

    TIME testing:

    The output for N = 20 but with different Restart vals, ran 30 times:
    N: 20
    Avg time:0.08s
    Restart val: 400 # Same as (N * N)

    N: 20
    Avg time:1.25s
    Restart val: 50 # Chosen randomly

With a bigger restart value, the algorithm generally is faster.
But too big of a restart value wont make it faster. 
If the restart value is too big, its the same as no restart value is assigned.
because, the line ``if iterations % RESTART_VALUE == 1:`` wont run
Generally the best restart values were in the range of 0.8 * (N * N) to 1.5 * (N * N)

Generally for bigger N values, a restart value is needed or the algorithm might get stuck
So we need to reset the board after some number of iterations.

The resetting is needed, because from some positions the global minimum (``best_value`` in code) can't be reached
with my used algorithm. So when we reset the board we, the starting state might be in the area where
global minimum is reachable by running the algorithm some iterations.

    The output for N = 100 done 2 times to find some pseudo avg time:
    0) Initial pos conflicts: 59
    Found in 36090 iterations, 37.09 seconds

    1) Initial pos conflicts: 54
    Found in 55263 iterations, 56.96 seconds

    N: 100
    Avg time:47.03s
    Restart val: 10000 # (N * N)
