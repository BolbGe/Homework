s = int(input())

mx = 0

for i in range(1, s):
    for j in range(1, s - i + 1):
        tmp = (i // 2) * (1 - (i % 2)) + (j // 2) * (1 - (j % 2))
        if tmp > mx:
            mx = tmp
            
print(mx)
        
                     

        
