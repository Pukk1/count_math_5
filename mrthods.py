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


def t_term_fun(x, nodes, counter, count_to):
    h = nodes[1][0] - nodes[0][0]
    t_fun = lambda arg: (arg - nodes[0][0]) / h
    if counter == count_to:
        return (t_fun(x) - counter + 1) / counter
    else:
        return t_term_fun(x, nodes, counter + 1, count_to) * (t_fun(x) - counter + 1) / counter


def newton_solution(x, nodes, counter, count_to):
    if counter == count_to:
        return find_delta_Y(0, nodes, counter) * t_term_fun(x, nodes, 1, counter)
    else:
        return newton_solution(x, nodes, counter + 1, count_to) + find_delta_Y(0, nodes, counter) * t_term_fun(x, nodes,
                                                                                                               1,
                                                                                                               counter)


def newton(nodes, x_arg):
    n = len(nodes)
    return nodes[0][1] + newton_solution(x_arg, nodes, 1, n - 1)
