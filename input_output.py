import math

import matplotlib.pyplot as plt
import numpy as np

function = {
    1: ["sin(x)", lambda x: math.sin(x)]
}


def paint(lagrange_method, newton_method, nodes, default_fun, searched_x):
    x = np.arange(nodes[0][0], nodes[len(nodes) - 1][0] + 0.01, 0.01)
    ax = plt.gca()

    computed_y = [newton_method(nodes, i) for i in x]
    ax.plot(x, computed_y, "red", linewidth=1.5)

    if default_fun is not None:
        computed_default_y = [default_fun(i) for i in x]
        ax.plot(x, computed_default_y, "blue", linewidth=1.5)
    nodes_x = [node[0] for node in nodes]
    nodes_y = [node[1] for node in nodes]
    plt.plot(nodes_x, nodes_y, 'o', color='blue')

    plt.plot(searched_x, newton_method(nodes, searched_x), 'o', color='red')
    plt.plot(searched_x, lagrange_method(nodes, searched_x), 'o', color='orange')

    # plt.xlabel('x - axis')
    plt.show()


def user_input():
    global function

    n = int(input("Введите количество узлов:"))
    nodes = [[0 for x in range(2)] for y in range(n)]

    example_fun = None
    if int(input("Введите 0 для ввода узлов или 1 для ввода функции-примера:")) == 0:
        for i in range(0, n):
            nodes[i][0] = float(input("X:"))
            nodes[i][1] = float(input("Y:"))
    else:
        for index, value in function.items():
            print(str(index), value[0])
        fun_num = int(input("Введите номер выбранной функции:"))
        example_fun = function[fun_num][1]
        a = int(input("Введите левый край промежутка:"))
        b = int(input("Введите правый край промежутка:"))
        for i in range(0, n):
            if i == n - 1:
                nodes[i][0] = b
            else:
                nodes[i][0] = (b+1 - a) / n * i + a
            nodes[i][1] = example_fun(nodes[i][0])
    x_arg = float(input("Введите точку в которой нужно найти значение функции:"))

    return n, nodes, x_arg, example_fun


def user_output(y_L, y_N):
    print("\n\nРезультат методом Лагранжа: ", str(y_L))
    print("Результат методом Ньютона: ", str(y_N))
