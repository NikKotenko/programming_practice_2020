import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-300, 300.01, 0.01)
plt.figure(figsize=(10, 5))
y = np.log((x*x+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x))))
plt.plot(x, y)
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid(True)
#plt.savefig('figure_with_legend.png')
plt.show()