file = open('sample.txt', 'r')

counter = 0

for line in file:
    counter += 1

file.close()

print(counter)
