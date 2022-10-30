

def f(n, walked):
    walked.append(n)
    if n < 1:
        return 0
    elif n == 1:
        for i in range(len(walked) - 2):
            if (walked[i] + walked[i+1] + walked[i+2]) % 11 == 0:
                print(n, walked)
                return 1
            else:
                return 0
    else:
       if n % 12 == 0:
           return f(n // 3, walked) + f(n // 4, walked) + f(n - 2, walked)
       elif n % 3 == 0:
           return f(n // 3, walked) + f(n - 2, walked)
       elif n % 4 == 0:
           return f(n // 4, walked) + f(n - 2, walked)
       else:
            return f(n - 2, walked)

print(f(600, []))
            
    
    