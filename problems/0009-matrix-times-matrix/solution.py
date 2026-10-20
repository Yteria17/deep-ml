def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    c = []
    for i in range(len(a)):
        tmp = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            tmp.append(total)
        c.append(tmp)
    return c