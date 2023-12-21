import json
import numpy as np

def compare(array):
    res = [[0 for i in range(len(array))] for i in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j]:
                res[i][j] = 0
            elif array[i] < array[j]:
                res[i][j] = 1
            else:
                res[i][j] = 0.5
    return res

def t_sum(array, n, m):
    res = 0
    for i in range(n):
      marks_numbers = {0:0, 0.5: 0, 1: 0}
      for j in range(m):
          for k in range(m):
              marks_numbers[array[i][j][k]] += 1
      for i in marks_numbers.values():
          res += (i**2 - i)
    return res

def task(string):
    input = json.loads(string)
    marks = []
    for elements in input:
        marks.append(compare(elements))

    n = len(marks)
    m = len(marks[0]) 

    marks_new = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):                                    
        for j in range(m):                                
            for k in range(m):                            
                marks_new[j][k] += marks[i][j][k]/n

    k0 = [1/m for i in range(n)]
    Eps = 0.001
    while True:
        y = np.matmul(marks_new, k0)
        lmbd = np.matmul([1,1,1], y)
        k = y / lmbd
        if Eps > max(k - k0):
          break
        else:
          k0 = k
    return k

if __name__ == "__main__":
    filename="data.csv"
    task(filename)
