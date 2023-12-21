import math

def matrix_prob(graph):
    pbm = []
    n = len(graph)
    for row in graph:
        temp_probs = []
        for value in row:
            temp_probs.append(float(value) / (n - 1))

        pbm.append(temp_probs)

    return pbm

def row_ent(pbm):
    ents = []

    for row in pbm:
        h = 0.0
        for value in row:
            if value != 0.0:
                h += -1 * value * math.log2(value)
        
        ents.append(h)
    
    return ents

def process(matrix):
    pbm = matrix_prob(matrix)
    ents = row_ent(pbm)

    entropy = 0.0
    for value in ents:
        entropy += value

    return entropy

if __name__ == "__main__":
    matrix = [[1,0,2,0,0],[2,1,2,0,0],[2,1,0,1,1],[0,1,0,1,1],[0,1,0,1,1],[0,1,0,1,1]]
    out = process(matrix)
    print(out)
