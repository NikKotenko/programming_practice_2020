import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 3.01, 0.01)
plt.figure(figsize=(15, 7.5))
a=3
n=1
y=0
for n in range(100):
    y=y+0.5**n*np.cos((a**n)*np.pi*x)
plt.plot(x, y )
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.grid()
#plt.savefig('figure_with_legend.png')
plt.show()