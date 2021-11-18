s = int(input())

mx = 0

for i in range(1, s):
    for j in range(1, s - i):
        tmp = i // 2 * (1 - (i % 2)) + ((j + 1) // 2) * (1 - (j + 1) % 2)
        if tmp > mx:
            mx = tmp
            
print(mx)
        
                     

        