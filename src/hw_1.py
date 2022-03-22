import numpy as np


def vec_mult(vec1, vec2):
    len_vec1 = len(vec1)
    len_vec2 = len(vec2)
    mult = sum(map(lambda x, y: x * y, vec1, vec2))
    return len_vec1, len_vec2, mult


def vec_angle(vec1, vec2):
    unit_vector_1 = vec1 / np.linalg.norm(vec1)
    unit_vector_2 = vec2 / np.linalg.norm(vec2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle


def mat_trans(matrix):
    trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans


def mat_add_mult(m1, m2):
    addition = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    multiplication = [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]
    return addition, multiplication


def wc(file_name):
    counts = {"lines": 0, "words": 0, "characters": 0}
    with open(file_name) as f:
        for line in f:
            counts["lines"] += 1
            counts["words"] += len(line)
            counts["characters"] += len(line.split())
        for key, value in counts.items():
            print(f"{key}:{value}")


def nl(file_name):
    count = 1
    with open(file_name) as f:
        for line in f:
            if line.isspace():
                print(f"\t{line.rstrip()}")
            else:
                print(f"{count}\t{line.rstrip()}")
                count += 1


def head(file_name):
    with open(file_name) as f:
        for i, line in enumerate(f):
            if i == 10:
                break
            print(line.rstrip())


def tail(file_name):
    with open(file_name) as f:
        reversed_lines = list(reversed(f.readlines()))
        print("".join(list(reversed(reversed_lines[:10]))))
