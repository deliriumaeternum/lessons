n = 3
m = 5
value = 42

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result = get_matrix(n, m, value)
print(result)
