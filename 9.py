import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra(graph, 0))  # Output: [0, 3, 1, 4]
