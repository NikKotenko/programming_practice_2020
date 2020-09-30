import numpy as np
import matplotlib.pyplot as plt

x = np.arange( -2 , 2 , 0.01)
y = np.log(np.exp(1/(np.sin(x)+ 1))/(5/4 + 1/(x**15)))/np.log(1+x*x)

plt.figure(figsize=(15, 7.5))
plt.plot(x, y )
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid()
plt.show()