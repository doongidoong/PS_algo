def floyd(n,graph):
    for i in range(n):
        graph[i][i] = 0  
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    return graph
