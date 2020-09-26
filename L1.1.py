import numpy as np
x = input()
y = np.log(np.exp(1/(np.sin(x)+ 1))/(5/4 + 1/(x**15)))/np.log(1+x*x)
print(y)
