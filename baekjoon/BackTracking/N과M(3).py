N, M = list(map(int, input().split()))

nums = []

def solution():
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return

    for i in range(1, N + 1):
        if len(nums) < M:
            nums.append(i)
            solution()
            nums.pop()

solution()
