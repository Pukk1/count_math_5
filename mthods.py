def lagrange(nodes, x):
    n = len(nodes)
    L = 0.0
    for i in range(0, n):
        s = 1.0
        for j in range(0, n):
            if i == j:
                continue
            s *= (x - nodes[j][0]) / (nodes[i][0] - nodes[j][0])
        L += nodes[i][1] * s
    return L


def find_delta_Y(index, nodes, degree):
    if (degree > 1):
        return find_delta_Y(index + 1, nodes, degree - 1) - find_delta_Y(index, nodes, degree - 1)
    return nodes[index + 1][1] - nodes[index][1]


def newton_from_0(nodes, x):
    n = len(nodes)
    N = nodes[0][1]
    h = nodes[1][0] - nodes[0][0]
    t = (x - nodes[0][0]) / h

    for i in range(1, n):
        delta_y = find_delta_Y(0, nodes, i)
        factor = 1

        for k in range(1, i + 1):
            factor *= (t - k + 1) / k

        N = N + factor * delta_y
    return N


def newton(nodes, x):
    # return newton_left(nodes, x)
    if x <= (nodes[len(nodes) - 1][0] - nodes[0][0]) / 2 + nodes[0][0]:
        return newton_left(nodes, x)
    else:
        return newton_right(nodes, x)


def newton_left(nodes, x):
    n = len(nodes)

    x0_pos = 0
    for i in range(1, n):
        if x <= nodes[i][0]:
            break
        x0_pos = x0_pos + 1

    N = nodes[x0_pos][1]
    h = nodes[x0_pos + 1][0] - nodes[x0_pos][0]
    t = (x - nodes[x0_pos][0]) / h

    print("\n\nLeft delta_l:")

    for i in range(1, n - x0_pos):
        delta_y = find_delta_Y(x0_pos, nodes, i)
        print(delta_y)
        factor = 1

        for k in range(1, i + 1):
            factor *= (t - k + 1) / k

        N = N + factor * delta_y
    return N


def newton_right(nodes, x):
    n = len(nodes)
    N = nodes[n-1][1]
    h = nodes[1][0] - nodes[0][0]
    t = (x - nodes[n-1][0]) / h
    print("\n\nRight delta_l:")
    for i in range(1, n):
        delta_y = find_delta_Y(n-1-i, nodes, i)
        factor = 1
        print(delta_y)
        for k in range(1, i + 1):
            factor *= (t + k - 1) / k

        N = N + factor * delta_y
    return N
