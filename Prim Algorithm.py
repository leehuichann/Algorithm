import heapq

def prim(n, graph, start=1):
    visited = [False] * (n + 1)
    pq = []
    mst = []
    total_weight = 0

    visited[start] = True

    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))  # (weight, u, v)

    while pq:
        w, u, v = heapq.heappop(pq)

        if visited[v]:
            continue

        # (u, v) 간선 선택
        visited[v] = True
        mst.append((u, v, w))
        total_weight += w

        for next_v, next_w in graph[v]:
            if not visited[next_v]:
                heapq.heappush(pq, (next_w, v, next_v))

    return mst, total_weight

# Graph 1 (왼쪽 그림)
graph1 = {
    1: [(2, 10), (4, 30), (5, 45)],
    2: [(1, 10), (5, 40), (3, 50)],
    3: [(2, 50), (5, 35), (6, 15)],
    4: [(1, 30), (6, 20)],
    5: [(1, 45), (2, 40), (3, 35), (6, 55)],
    6: [(4, 20), (5, 55), (3, 15), (2, 25)]
}

graph1 = {k: v for k, v in graph1.items()}

# Graph 2 (오른쪽 그림)
graph2 = {
    1: [(2, 16), (6, 21), (5, 19)],
    2: [(1, 16), (6, 11), (3, 5), (4, 6)],
    3: [(2, 5), (4, 10)],
    4: [(2, 6), (3, 10), (6, 14), (5, 18)],
    5: [(1, 19), (6, 33), (4, 18)],
    6: [(1, 21), (2, 11), (4, 14), (5, 33)]
}

graph2 = {k: v for k, v in graph2.items()}

# 실행
print("----- Graph 1: MST -----")
mst1, w1 = prim(6, graph1)
for e in mst1:
    print(e)
print("MST Total Weight:", w1)

print("\n----- Graph 2: MST -----")
mst2, w2 = prim(6, graph2)
for e in mst2:
    print(e)
print("MST Total Weight:", w2)
