x = list(map(int, input().split()))
y = int(input())
def f(x, y, n, ln, k):
    n -= 1
    if n == 0:
        return x, 0
    mx = 0
    indmx = 0
    for i in range(1, 10):
        if x.count(i) != 0:
            ind = x.index(i)
            tmp = x[0:]
            tmp[0], tmp[ind] = tmp[ind], tmp[0]
            delta = f(tmp, y, n, ln, k)[1]
            if delta > mx:
                indmx = ind
                mx = delta
    x[0], x[indmx] = x[indmx], x[0]
    return [x[0], ] + f(x[1:], y, n, ln, k)[0], k + f(x[1:], y, n, ln, k)[1] - indmax


print(f(x, y, len(x)-1, len(x)-1, 0))
            
    
    
    
    
