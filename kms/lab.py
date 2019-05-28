import numpy as np


def result():
    b = [2, -3]
    x = [[2, 5, 8, 6, 3, 6], [5, 8, 4, 1, 7, 2]]
    y = []
    for i in range(6):
        y.append(round(b[0] * x[0][i] + b[1] * x[1][i], 3))
    f = [[1, 2, 5, 10, 4, 25],
         [1, 5, 8, 40, 25, 64],
         [1, 8, 4, 32, 64, 16],
         [1, 6, 1, 6, 36, 1],
         [1, 3, 7, 21, 9, 49],
         [1, 6, 2, 12, 36, 4]
         ]
    f = np.array(f)
    c = np.linalg.inv((np.matmul(np.matrix.transpose(f), f)))
    b_b = np.matmul(np.matmul(c, np.matrix.transpose(f)), np.array(y))
    q = [1 / np.linalg.norm(i) for i in c]
    a_cs = np.matmul(np.reshape(b_b, (1, 6)), q)
    w, v = np.linalg.eig(c)
    lambda_max = max(w)
    lambda_max = lambda_max / 400
    lambda_i = [abs(sum(i)) for i in v]
    k_c = [lambda_max / i for i in lambda_i]
    m_c = []
    for i in k_c:
        if i >= 0.5:
            m_c.append(2 - (1 / i))
        else:
            m_c.append(0)

    b_c = [i - np.matmul(m_c, np.reshape(q, (6, 1))) * a_cs for i in b_b]

    answer = np.linalg.norm(b_c)

    w1, v1 = np.linalg.eig((np.matmul(np.matrix.transpose(f), f)))
    alpha = np.matmul(v1, b_b)
    delta = 1 - 0.1 * (1 - 0.5625) / 0.5625
    alpha_js = [i * delta for i in alpha]
    b_rm = np.matmul(np.linalg.inv((np.matmul(np.matrix.transpose(f), f)) + (1 / 0.01) * np.identity(6)),
                     np.matmul(np.matrix.transpose(f), np.array(y)))
    minmax = np.matmul(np.matrix.transpose(alpha), b_rm)

    return b_c, answer, alpha_js, minmax