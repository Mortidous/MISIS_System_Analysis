import numpy as np
import json
import sys

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def flatten(range_r):
    return [j for i in range_r for j in (i if isinstance(i, list) else [i])]


def find_ind(range_r, x):
    return next((i for i, subrange in enumerate(range_r) if x in subrange), None)


def parse_range(r):
    return [[x] if isinstance(x, int) else x for x in r]


def calc_matrix(r):
    n = max(flatten(r))
    matrix = [[1 if find_ind(r, j + 1) >= find_ind(r, i + 1) else 0 for j in range(n)] for i in range(n)]
    return matrix

def find_conflicts(m1, m2):
    y1, y2 = np.array(m1), np.array(m2)
    conflicts = np.logical_or(np.multiply(y1, y2), np.multiply(y1.T, y2.T)).astype(int)
    res = [[j + 1, i + 1] for i in range(len(conflicts)) for j in range(i) if conflicts[i][j] == 0]
    return unite_conflicts(res)


def unite_conflicts(c):
    n = len(c)
    for _ in range(n):
        res, to_skip = [], []
        for i, p1 in enumerate(c):
            if i in to_skip:
                continue
            merged = np.unique([x for j, p2 in enumerate(c) for x in p2 if j > i and set(p1) & set(p2)])
            if merged.size:
                merged.sort()
                res.append(merged)
                to_skip.extend(j for j, p2 in enumerate(c) if j > i and set(p1) & set(p2))
            else:
                res.append(np.array(p1))
        c = res
    return c


def find_common_range(a, b, conflicts):
    result, used = [], []
    for cl in a + b:
        for value in cl:
            if value in used:
                continue
            cluster = next((cluster for cluster in conflicts if value in cluster), None)
            if cluster is not None:
                if all(item in used for item in cluster):
                    continue
                result.append(cluster.tolist())
                used.extend(cluster)
            else:
                result.append(value)
                used.append(value)
    return result


def task(a, b):
    a_parsed, b_parsed = parse_range(a), parse_range(b)
    matrix_a, matrix_b = calc_matrix(a_parsed), calc_matrix(b_parsed)
    conflicts_ab = find_conflicts(matrix_a, matrix_b)
    return find_common_range(a_parsed, b_parsed, conflicts_ab)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Введите две json-строки, содержащие ранжировки.")

    a_file, b_file = sys.argv[1], sys.argv[2]
    a, b = read_json_from_file(a_file), read_json_from_file(b_file)
    print(task(a, b))

#a = "[1,[2,3],4,[5,6,7],8,9,10]"
#b = "[[1,2],[3,4,5],6,7,9,[8,10]]"
#c = "[3,[1,4],2,6,[5,7,8],[9,10]]"