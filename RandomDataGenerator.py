import random
import time

with open('DG.txt', 'w') as fl:
    # count of number in a row
    number_in_row = 2

    # Count of lines
    lines = 1500

    Start = time.time()

    for _ in range(lines):
        IN = [random.randint(0, 100000) for _ in range(number_in_row)]
        # Space or any separators u want
        tmp = ''.join(str(IN)[1:-1].split(','))

        fl.write(tmp + '\n')

print('Time : ', time.time() - Start)