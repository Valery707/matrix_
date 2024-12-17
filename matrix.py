def get_matrix (n,m,v):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(v)
    return matrix
r1 = get_matrix(2,2,10)
print (r1)
r2 = get_matrix(3,5,42)
print (r2)
r3 = get_matrix(4,2,13)
print (r3)