N, M = list(map(int, input().split()))

nums = []

def solution():
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return

    for i in range(1, N + 1):
        if i not in nums:
            nums.append(i)
            solution()
            nums.pop()

solution()