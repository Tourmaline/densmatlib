import matplotlib.pyplot as plt
import numpy as np

N = np.array([1000, 2000, 5000, 10000])
Tdiag = np.array([0.1996, 1.636, 23.156, 230.466])
Trecexp = np.array([0.707, 5.341, 88.363, 698.978])
plt.figure(1)
plt.plot(N, Tdiag, '-or', N, Trecexp, '-*b')
plt.show()


plt.figure(2)
plt.plot(N, Trecexp/Tdiag, '-*b')
plt.show()

