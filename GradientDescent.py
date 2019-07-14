import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

plt.plot(X, y, 'b.')
plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
_ = plt.axis([0, 2, 0, 15])
plt.show()
