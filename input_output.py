import matplotlib.pyplot as plt
import numpy as np


def paint(lagrange_method, newton_method, nodes, default_fun, searched_x):
    x = np.arange(nodes[0][0], nodes[len(nodes) - 1][0] + 0.01, 0.01)
    ax = plt.gca()

    computed_y = [newton_method(nodes, i) for i in x]
    ax.plot(x, computed_y, "red", linewidth=1.5)
    # computed_y = [method(nodes, node[0]) for node in nodes]
    # computed_x = [node[0] for node in nodes]
    # plt.plot(computed_x, computed_y, 'o', color='red')

    if default_fun is not None:
        computed_default_y = [default_fun(i) for i in x]
        ax.plot(x, computed_default_y, "blue", linewidth=1.5)
    else:
        nodes_x = [node[0] for node in nodes]
        nodes_y = [node[1] for node in nodes]
        plt.plot(nodes_x, nodes_y, 'o', color='blue')

    plt.plot(searched_x, newton_method(nodes, searched_x), 'o', color='black')
    plt.plot(searched_x, lagrange_method(nodes, searched_x), 'o', color='orange')

    plt.xlabel('x - axis')
    plt.show()


def user_input():
    n = int(input("Введите количество узлов:"))
    nodes = [[0 for x in range(2)] for y in range(n)]

    example_fun = None
    if int(input("Введите 0 для ввода узлов или 1 для ввода функции-примера:")) == 0:
        for i in range(0, n):
            nodes[i][0] = float(input("X:"))
            nodes[i][1] = float(input("Y:"))
    else:
        example_fun = None
    x_arg = float(input("Введите точку в которой нужно найти значение функции:"))

    return n, nodes, x_arg, example_fun


def user_output(y_L, y_N):
    print("\n\nРезультат методом Лагранжа: ", str(y_L), "\nРезультат методом Ньютона: ", str(y_N))
