import random
import time

# Random Data Generator


fl = open('DG.txt', 'w')

# count of number in a row
number_in_row = 2

# Count of lines
lines = 1500

Start = time.time()

for i in range(lines):
    IN = []
    for num in range(number_in_row):
        IN.append(random.randint(0, 100000))
    # Space or any separators u want
    tmp = ''.join(str(IN)[1:-1].split(','))

    fl.write(tmp + '\n')

fl.close()

print('Time : ', time.time() - Start)