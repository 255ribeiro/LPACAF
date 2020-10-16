import matplotlib.pyplot as plt
import numpy as np
x =list(range(0,11,2))
y = []
z =[]
for i in x:
    y1 = np.random.random()
    z1 = np.random.random()

    y.append(y1)
    z.append(z1)


fig = plt.figure(figsize=(10,5))
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(x,y,color='y', linewidth=10, marker='s', ms=15, markerfacecolor='b')
l2 = ax.plot(x,z,'go--')
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right')
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()