from input_output import user_input
from mrthods import lagrange, newton
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    (n, nodes, x_arg, example_fun) = user_input()
    N = newton(nodes, x_arg)
    print(N(0.35))
