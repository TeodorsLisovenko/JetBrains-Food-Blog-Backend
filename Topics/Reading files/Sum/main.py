file = open('sums.txt', 'r')

for line in file:
    values = line.split()
    print(int(values[0]) + int(values[1]))

file.close()
