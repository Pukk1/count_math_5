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


# def newton(nodes, x):
#     # нужна валидация
#
#     n = len(nodes)
#     x0_pos = 0
#     for i in range(1, n):
#         if x <= nodes[i][0]:
#             break
#         x0_pos = x0_pos + 1
#
#     N = nodes[x0_pos][1]
#     # h - шаг интерполирования
#     h = nodes[x0_pos + 1][0] - nodes[x0_pos][0]
#     t = (x - nodes[x0_pos][0]) / h
#
#     for i in range(1, n - x0_pos):
#         temp = find_delta_Y(x0_pos, nodes, i)
#         for k in range(1, i + 1):
#             temp = temp * (t - k + 1) / k
#         N = N + temp
#     return N


def find_delta_Y(index, nodes, degree):
    if (degree > 1):
        return find_delta_Y(index + 1, nodes, degree - 1) - find_delta_Y(index, nodes, degree - 1)
    return nodes[index + 1][1] - nodes[index][1]


def newton(nodes, x_arg):
    n = len(nodes)
    N = nodes[0][1]
    h = nodes[1][0] - nodes[0][0]
    t = (x_arg - nodes[0][0]) / h

    for i in range(1, n):
        delta_y = find_delta_Y(0, nodes, i)
        factor = 1

        for k in range(1, i + 1):
            factor *= (t - k + 1) / k

        N = N + factor * delta_y
    return N
