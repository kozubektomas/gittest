import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,11)
y=np.sin(x)

for i in range(0,11):
  print("(%.2f,%.2f)" % (x[i],y[i]))

fig, axis = plt.subplots()
axis.plot(x,y,'r-')
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_title('Test')
plt.show()
