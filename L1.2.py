import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2, 3.01, 0.01)
plt.figure(figsize=(10, 5))
plt.plot(x, x*x - x - 6, label=r'$f_1(x) =\ x^2-x+6 $')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
#plt.savefig('figure_with_legend.png')
plt.show()