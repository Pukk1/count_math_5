from input_output import user_input, paint, user_output
from mthods import newton, lagrange, newton_from_0

if __name__ == '__main__':
    # try:
        (n, nodes, x, example_fun) = user_input()
        paint(lagrange, newton_from_0, nodes, example_fun, x)
        user_output(lagrange(nodes, x), newton(nodes, x))
    # except:
        # print("Что-то сломалось!")
