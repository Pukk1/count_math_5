def lagrange(nodes, x_arg):
    n = len(nodes)
    L = 0.0
    for i in range(0, n):
        s = 1.0
        for j in range(0, n):
            if i == j:
                continue
            s *= (x_arg - nodes[j][0]) / (nodes[i][0] - nodes[j][0])
        L += nodes[i][1] * s
    return L


def find_delta_Y(index, nodes, degree):
    if (degree > 0):
        return nodes[index + 1][1] - nodes[index][1]
    return find_delta_Y(index + 1, nodes, degree - 1) - find_delta_Y(index, degree - 1)


def find_T_factor(nodes, index, x_arg):
    h = nodes[1][0] - nodes[0][0]
    t_fun = lambda x: (x - nodes[0][0]) / h
    term_fun = None
    for k in range(1, index + 1):
        term_fun = lambda x: term_fun(x) * (t_fun(x) - k + 1) / k
    return term_fun(x_arg)


def newton(nodes, x_arg):
    n = len(nodes)
    N_fun = lambda x: x
        # nodes[0][1]

    for i in range(1, n):
        print(i)
        N_fun = lambda x: N_fun(x)

    for i in range(1, n):
        delta_Y = find_delta_Y(0, nodes, i)

        # N_fun = lambda x: N_fun(x)
                          # + delta_Y
                          # * find_T_factor(nodes, i, x)
    return N_fun
