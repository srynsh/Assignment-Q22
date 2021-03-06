import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})
x1 = np.linspace(0,5000,1000)

y1 = x1*x1/100 + 100*x1 + 40
y2 = 200*x1 - x1*x1/400
y3 = 100 - x1/40

plt.plot(x1, y3) #The solpe which is so small that it is not visible.

plt.plot(x1,y1, label='$Total\ Cost = x^{2}/100 + 100x + 40$')
plt.plot(x1,y2,label='$P(x) = 200x - x^{2}/400$')
plt.plot(x1,y2-y1, label='$Total\ Profit = 100 - x/40$')

plt.plot(4000, 199960, marker = 'o', markersize = 5, markerfacecolor = 'blue')

plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")

plt.xlabel("Number of units")
plt.ylabel("Cost")
plt.grid()
plt.legend(loc='best', prop={'size':11})
plt.show()
