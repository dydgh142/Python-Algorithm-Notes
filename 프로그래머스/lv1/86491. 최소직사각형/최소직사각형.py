def solution(sizes):
    # max(max(x) for x in sizes) -> [60,50] 중 큰 숫자들을 모아 그중 큰 수를 고름
    # max(min(x) for x in sizes) -> [60,50] 중 50, 작은숫자들중 가장 큰 수를 고름
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)