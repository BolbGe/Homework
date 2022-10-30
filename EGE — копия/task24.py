with open('24.txt', 'r') as file:
    data = file.read()
    
alp = 'A1B1A2B2'

mx = 0
counter = 0
i = 0
lastPair = False
for i in range(0, len(data)-1, 2):
    if not lastPair and data[i] + data[i+1] in alp:
        counter += 1
        lastPair = True
    if lastPair and not data[i] + data[i+1] in alp:
        if counter > mx:
            mx = counter
        counter = 0
        lastPair = False
    if lastPair and data[i] + data[i+1] in alp: 
        counter += 1
counter = 0
mn = 0      
for i in range(1, len(data)-1, 2):
    if not lastPair and data[i] + data[i+1] in alp:
        counter += 1
        lastPair = True
    if lastPair and not data[i] + data[i+1] in alp:
        if counter > mn:
            mn = counter
        counter = 0
        lastPair = False
    if lastPair and data[i] + data[i+1] in alp: 
        counter += 1
        

        

print(max(mx, mn))