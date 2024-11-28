def floyd_warshall(matrix):
    n = len(matrix)
    dist = [[float('inf') if matrix[i][j] == -1 else matrix[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

matrix = [[0, 3, -1], [2, 0, -1], [-1, 7, 0]]
print(floyd_warshall(matrix))
