# 202315167 컴퓨터과학전공 이희찬
# 0/1 Knapsack - Memoization

# i번째 물건까지 고려했을 때, 남은 용량이 rest 일 때 얻을 수 있는 최대 이익을 반환
def knap(i, rest, w, p, cache):
    # 물건이 없거나 남은 용량이 0인 경우
    if i == 0 or rest == 0:
        return 0

    # Memoization 확인
    if cache[i][rest] != -1:
        return cache[i][rest]

    idx = i - 1

    # 무게 초과 시 물건을 담지 못하는 경우
    if w[idx] > rest:
        cache[i][rest] = knap(i - 1, rest, w, p, cache)
    else:
        take = p[idx] + knap(i - 1, rest - w[idx], w, p, cache)
        not_take = knap(i - 1, rest, w, p, cache)
        cache[i][rest] = max(take, not_take)

    return cache[i][rest]


# 선택된 물건들을 복원하는 함수
def reconstruct(n, M, w, p, cache):
    selected = []
    i = n
    rest = M

    while i > 0 and rest > 0:
        # i번째 물건을 사용 X
        if cache[i][rest] == cache[i - 1][rest]:
            i -= 1
        else:
            # i번째 물건을 사용 O
            selected.append(i)
            rest -= w[i - 1]
            i -= 1

    selected.reverse()
    return selected

if __name__ == "__main__":
    n = 6
    M = 100
    p = [40, 35, 18, 4, 10, 2]          # 이익 (p1 ~ p6)
    w = [100, 50, 45, 20, 10, 5]        # 무게 (w1 ~ w6)

    cache = [[-1] * (M + 1) for _ in range(n + 1)]

    max_profit = knap(n, M, w, p, cache)
    picked = reconstruct(n, M, w, p, cache)

    print("최대 이익:", max_profit)
    print("선택된 물건 번호:", picked)

    # 합산 무게와 이익 출력
    total_w = sum(w[i - 1] for i in picked)
    total_p = sum(p[i - 1] for i in picked)
    print("선택된 물건들의 총 무게:", total_w)
    print("선택된 물건들의 총 이익:", total_p)
