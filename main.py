from input_output import user_input, paint
from mrthods import lagrange, newton, default_newton

if __name__ == '__main__':
    (n, nodes, x, example_fun) = user_input()
    paint(default_newton, nodes, None, x, default_newton(nodes, x))
