import time
import pandas

# Data Set Generator
from sklearn.datasets import make_circles, make_blobs, make_moons

# fl = open('DG.csv', 'w')

Start = time.time()


# Features = m

tmp = make_circles(n_samples=700, noise=0.04)
# tmp = make_blobs(n_samples=700, centers=4, n_features=2)
# tmp = make_moons(n_samples=700, noise=0.1)


# for i in tmp[0]:
#     fl.write(str(i[0]) + ' ' + str(i[1]) + '\n')


# data = pandas.ExcelWriter(tmp[0])
data = pandas.DataFrame(tmp[0])
data.to_excel('ExcelData.xlsx')
# print(data)

# fl.close()

print('Time : ', time.time() - Start)
