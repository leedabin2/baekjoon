import sys

N = int(sys.stdin.readline().rstrip())

a = N // 10  # 첫번째 값
b = N - ((N // 10) * 10)  # 두번째 값

cnt = 0
def dfs(n,count):
    global cnt

    if n == N and count >0:
        cnt = count
        return cnt

    else:
        a = n // 10  # 첫번째 값
        b = n - ((n // 10) * 10)  # 두번째 값
        new = b * 10 + (a+b) % 10
        return dfs(new,count+1)

res = dfs(N,0)
print(res)