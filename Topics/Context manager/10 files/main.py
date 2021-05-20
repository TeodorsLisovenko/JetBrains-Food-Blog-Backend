for x in range(1, 11):
    with open(f'file{x}.txt', 'w') as f:
        f.write(str(x))
