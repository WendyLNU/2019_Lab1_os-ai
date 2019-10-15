global N  # 皇后个数
global SUM  # 当前已找到的可行方案数
N = 4
SUM = 0
def print_solution(x):
    for i in range(len(x)):
        print('.'*x[i]+'x'+'.'*(4-x[i]-1))
    print()
def is_safe(k):
    for i in range(k):
        if x[i] == x[k]:
            return False
        if (x[i] - x[k]) == (i - k):
            return False
        if (x[i] - x[k]) == (k - i):
            return False
    return True
def backtrack(t):
    global SUM
    if t >= N:
        SUM += 1
        print_solution(x)
    else:
        for i in range(N):
            x[t] = i
            if is_safe(t):
                backtrack(t + 1)
if __name__ == "__main__":
    x = [0 for i in range(N)]
    backtrack(0)
    print("sum =" + str(SUM))
