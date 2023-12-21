import csv

def writing(file_name):
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['0', '1', '0', '0', '0', '0'])
        writer.writerow(['-1', '0', '1', '1', '0', '0'])
        writer.writerow(['0', '-1', '0', '0', '1', '1'])
        writer.writerow(['0', '-1', '0', '0', '0', '0'])
        writer.writerow(['0', '0', '-1', '0', '0', '0'])
        writer.writerow(['0', '0', '-1', '0', '0', '0'])

def reading(file_name):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=';')
        matrix = []
        for row in reader:
            matrix.append(row)
        return matrix

def task(matrix):
    res = []
    for i in range(len(matrix)):
        res.append([0, 0, 0, 0, 0])
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                res[i][0] += 1
                for k in matrix[j]:
                    if k == '1':
                        res[i][2] += 1
            if matrix[i][j] == '-1':
                res[i][1] += 1
                for k in matrix[j]:
                    if k == '-1':
                        res[i][3] += 1
                    if k == '1':
                        res[i][4] += 1
    for st in res:
        if st[4]:
            st[4] -= 1
    with open('task2.csv', "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for st in res:
            writer.writerow(st)
    return res

if __name__ == "__main__":
    file_name = input()
    writing(file_name)
    matrix = reading(file_name)
    print(*task(matrix), sep='\n')
