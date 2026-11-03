

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

def func(x):
    
    return np.sinc(x)

x = np.linspace(-4, 4, 100)

plt.plot(x, func(x), label="Test func")
plt.title("Test")
plt.xlabel("x-test")
plt.ylabel("y-test")
plt.legend()
plt.show()