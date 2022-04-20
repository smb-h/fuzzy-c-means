import time

# Data Set Generator
from sklearn.datasets import make_circles, make_blobs, make_moons

with open('DG.csv', 'w') as fl:
    Start = time.time()


    # Features = m

    # tmp = make_circles(n_samples=300, noise=0.05)
    # tmp = make_blobs(n_samples=500, centers=4, n_features=2)
    # tmp = make_moons(n_samples=300, noise=0.1)
    tmp = make_blobs(n_samples=10, centers=4, n_features=2)


    for i in tmp[0]:
        fl.write(f'{str(i[0])} {str(i[1])}' + '\n')

print('Time : ', time.time() - Start)
