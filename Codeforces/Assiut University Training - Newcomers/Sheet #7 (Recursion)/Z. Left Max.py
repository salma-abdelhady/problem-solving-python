n = int(input())
arr = list(map(int, input().split()))

arr_ans = []
ma = arr[0]
for i in range(n):
    ma = max(ma, arr[i])
    arr_ans.append(ma)

print(*arr_ans)
