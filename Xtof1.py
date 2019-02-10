import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7 + 1)
internet = 90*x
direct_connect = 20*x + 216
plt.title("Price per Tb")
plt.plot(x, internet, label = "Internet")
plt.plot(x, direct_connect, label = "Direct connect")
plt.xlabel("Tb")
plt.ylabel("Price ($)")
plt.grid(True)
plt.legend()
plt.show()