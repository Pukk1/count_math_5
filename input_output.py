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
