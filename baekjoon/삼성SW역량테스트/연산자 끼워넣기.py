N = int(input())
nums = list(map(int, input().split()))
oper_cnt = list(map(int, input().split()))
global max_val
max_val = -1e9
global min_val
min_val = 1e9


def solution(N, nums, oper_cnt, oper_arr):
    global max_val
    global min_val
    operation = ['+', '-', '*', '//']

    if len(oper_arr) == N - 1:
        answer = nums[0]

        for i in range(1, N):
            if oper_arr[i - 1] == '+':
                answer += nums[i]
            elif oper_arr[i - 1] == '-':
                answer -= nums[i]
            elif oper_arr[i - 1] == '*':
                answer *= nums[i]
            else:
                if answer < 0:
                    answer = -(-answer // nums[i])
                else:
                    answer //= nums[i]

        max_val = max(answer, max_val)
        min_val = min(answer, min_val)

        return

    for i in range(4):
        if oper_cnt[i] > 0:
            oper_arr.append(operation[i])
            oper_cnt[i] -= 1
            solution(N, nums, oper_cnt, oper_arr)
            oper_cnt[i] += 1
            oper_arr.pop()

    return

solution(N, nums, oper_cnt, [])
print(max_val)
print(min_val)