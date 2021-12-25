#n = int(input())
#friends = list(map(int, input().split()))


def f(l):
    dp = []
    if len(l) == 2:
        return 1
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            l.pop(i)
            l.pop(i-1)
            return f(l) + 1
    
    for i in range(1, len(l)):
        tmp = l[0:len(l)]
        tmp[i] = tmp[i-1]
        dp.append(f(tmp))
    return min(dp) + 1

print(f([4, 2, 3, 2, 4, 3]))
        