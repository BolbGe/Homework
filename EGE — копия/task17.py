with open('17.txt', 'r') as file:
    data = file.read()

data = list(map(int, data.split('\n')))

mx = 0
counter = 0

for i in range(len(data) - 1):
    for j in range(i, len(data)):
        smallSum = (data[i] + data[j])
        if smallSum % 120 == 0:
            counter += 1
            if smallSum > mx:
                mx = smallSum
print(counter, mx)