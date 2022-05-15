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


def newton(nodes, x_arg):
    n = len(nodes)
    N = nodes[0][1]
    h = nodes[1][0] - nodes[0][0]
    t = (x_arg - nodes[0][0]) / h

    for i in range(1, n):
        term_fun = find_delta_Y(0, nodes, i)

        for k in range(1, i + 1):
            term_fun = term_fun * (t - k + 1) / k

        N = N + term_fun
    return N
