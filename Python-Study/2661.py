# 좋은 수열
# 좋은 수열 중 가장 작은 값을 출력해라.
import sys

def check(arr):
    #검사 하러 온 수열의 길이 arr_len
    arr_len = len(arr)
    #비교 해야할 횟수만큼 돌림
    for part_len in range(1, arr_len // 2 + 1):
        # 부분수열 비교 시작
        for part_start in range(part_len, arr_len - part_len + 1):
            # 같은 부분수열 발견하면
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False			# False 리턴
    else:					# 모든 부분수열이 다르면
        return True				# True 리턴

# 백트래킹 (두번째 자릿수, 처음 길이)
def dfs(arr, depth):
    # 압력받은 길이가 된다면
    if depth == N:
        print("".join(list(map(str, arr))))	# 수열 출력
        sys.exit()				# 종료

    arr.append(1)				# 1 추가 (아무 수나 상관 없음)
    for i in range(1, 4):			# 1부터 3까지  넣어보며
        arr.pop()
        arr.append(i)
        #좋은 수열인지 판단. 좋다면
        if check(arr):
            #다음 자리수 이어서 진행
            if not dfs(arr, depth + 1):
            # 만약 다음 자리 수에서 1~3 모두 넣어도 좋은 수열이 없다면 현재 자리수 1 증가
                continue
    else:
        # 현재 자리 수 1~3 모두 넣어도 좋은 수열이 없는 경우
        arr.pop()				# 이번 자리 수 없앰
        return False				# False 리턴


N = int(input())
dfs([1], 1)