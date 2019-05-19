import itertools
import numpy as np


def johnson(matrix):
    """
    Johnson method of create release plan
    :param matrix:
    :return: release plan
    """

    # division on group
    first_group = []
    second_group = []
    for key in matrix:
        if matrix[key][0] + matrix[key][1] < matrix[key][1] + matrix[key][2]:
            first_group.append(key)
        else:
            second_group.append(key)

    # sort first group
    arr_first = []
    for i in first_group:
        arr_first.append(matrix[i][0] + matrix[i][1])
    arr_first.sort()

    # sort second group
    arr_second = []
    for i in second_group:
        arr_second.append(matrix[i][1] + matrix[i][2])
    arr_second.sort(reverse=True)

    # sorted first group
    first_group_sorted = []
    for j in arr_first:
        for key in matrix:
            if (key in first_group) and j == matrix[key][0] + matrix[key][1]:
                if key in first_group_sorted:
                    break
                else:
                    first_group_sorted.append(key)

    # sorted second group
    second_group_sorted = []
    for j in arr_second:
        for key in matrix:
            if (key in second_group) and j == matrix[key][1] + matrix[key][2]:
                second_group_sorted.append(key)

    # final table
    final_arr = first_group_sorted + second_group_sorted
    return final_arr


def create_diagram(matrix, plan):
    """

    :param plan:
    :param matrix:
    :return: diagram with time
    """
    final_arr = plan
    diagram = [[[0, 0], [0, 0], [0, 0]] for i in range(len(matrix) + 1)]
    for i in range(len(diagram)):
        if i == 0:
            pass
        else:
            diagram[i][0][0] = diagram[i - 1][0][1]
            diagram[i][0][1] = diagram[i][0][0] + matrix[final_arr[i - 1]][0]
            diagram[i][1][0] = diagram[i][0][1] if diagram[i][0][1] >= diagram[i - 1][1][1] else diagram[i - 1][1][1]
            diagram[i][1][1] = diagram[i][1][0] + matrix[final_arr[i - 1]][1]
            diagram[i][2][0] = diagram[i][1][1] if diagram[i][1][1] >= diagram[i - 1][2][1] else diagram[i - 1][2][1]
            diagram[i][2][1] = diagram[i][2][0] + matrix[final_arr[i - 1]][2]
    return diagram


def full_bout(matrix):
    # return list of full boat of matrix
    return list(itertools.permutations([key for key in matrix]))


def standard(diagram):
    """
    calculate standard
    :param diagram:
    :return:
    """
    max_time = diagram[-1][-1][-1]

    k_1_1 = max_time
    k_1_2 = max_time
    k_1_3 = max_time

    t_p = []
    for i in range(3):
        temp = []
        for j in range(len(diagram) - 1):
            temp.append(abs(diagram[j][i][1] - diagram[j + 1][i][0]))
        t_p.append(temp)

    t_r = []
    for i in range(3):
        t_r.append(diagram[-1][i][1] - sum(t_p[i]))

    k_z = []
    for i in range(3):
        k_z.append(t_r[i] / diagram[-1][i][1])

    k_2_1 = min(k_z)
    k_2_2 = round(sum(k_z), 3)

    max_p = []
    for i in range(3):
        max_p.append(max(t_p[i]))
    k_2_3 = max(max_p)

    max_p = []
    t_p_m_o = []
    for i in range(3):
        t_p_m_o.append(t_p[i][1:])
    for i in range(3):
        max_p.append(max(t_p_m_o[i]))
    k_2_4 = max(max_p)

    sum_of = []
    for i in range(3):
        sum_of.append(sum(t_p[i]))
    k_2_5 = sum(sum_of)

    N_k = []
    for i in range(3):
        temp = []
        temp.append(1)
        for j in range(1, len(diagram) - 1):
            if t_p[i][j] != 0:
                temp.append(1)
        N_k.append(sum(temp))

    average = []
    for i in range(3):
        average.append(sum(t_p[i]) / N_k[i])
    k_2_6 = max(average)

    k_2_7 = sum(average)

    y_och = []
    for i in range(1, len(diagram)):
        temp = []
        temp.append(diagram[i][0][0])
        temp.append(diagram[i][1][0] - diagram[i][0][1])
        temp.append(diagram[i][2][0] - diagram[i][1][1])
        y_och.append(temp)

    max_of = []
    for i in y_och:
        max_of.append(max(i))
    k_3_1 = max(max_of)

    sum_of = []
    for i in y_och:
        sum_of.append(sum(i))
    k_3_2 = max(sum_of)
    k_3_3 = sum(sum_of)

    k_3_4 = k_3_2 / 3
    k_3_5 = k_3_2 / 3

    k_3_6 = round(k_3_3 / 3, 3)
    k_3_7 = round(k_3_3 / (len(diagram)-1), 3)
    list_standard = [k_1_1, k_1_2, k_1_3, k_2_1, k_2_2, k_2_3, k_2_4, k_2_5, k_2_6, k_2_7, k_3_1, k_3_2, k_3_3, k_3_4, k_3_5, k_3_6, k_3_7]
    list_standard = [round(i, 3) for i in list_standard]
    return list_standard


def create_optimize(matrix):
    """
    :param matrix:
    :return: extreme of standard
    """
    all_bout = []
    for i in full_bout(matrix):
        all_bout.append(standard(create_diagram(matrix, i)))

    all_column = np.array(all_bout).transpose()
    extreme = []
    for i in range(17):
        if i in (3, 4):
            extreme.append(max(all_column[i]))
        else:
            extreme.append(min(all_column[i]))
    return extreme, all_bout


def create_r(matrix):

    extreme_values, all_bout = create_optimize(matrix)
    compromise = []
    for i in range(len(all_bout)):
        temp = []
        for j in range(len(extreme_values)):
            temp.append(abs(extreme_values[j] - all_bout[i][j]))
        compromise.append(sum(temp))
    answer = compromise.index(min(compromise))
    return answer, compromise


# if __name__ == "__main__":
#     matr = {
#         '1': [3, 4, 4],
#         '2': [6, 3, 3],
#         '3': [4, 5, 4],
#         '4': [5, 2, 6]
#     }
#     # matr = {
#     #     '1': [1, 4, 6],
#     #     '2': [1, 1, 5],
#     #     '3': [2, 6, 6],
#     #     '4': [3, 4, 1]
#     # }
#     # print(johnson(matr))
#     # print(create_diagram(matr, johnson(matr)))
#     # print(full_bout(matr))
#     # print(standard(create_diagram(matr, full_bout(matr)[0])))
#     ans, all_compromise = create_r(matr)
#     print(ans)
#     print(full_bout(matr)[ans])
#     print(create_diagram(matr, full_bout(matr)[ans]))
#     print(johnson(matr))

