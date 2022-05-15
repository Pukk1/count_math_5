from input_output import user_input, paint, user_output
from mrthods import newton, lagrange

if __name__ == '__main__':
    (n, nodes, x, example_fun) = user_input()
    paint(lagrange, newton, nodes, None, x)
    user_output(lagrange(nodes, x), newton(nodes, x))
