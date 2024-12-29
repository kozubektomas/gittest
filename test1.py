import numpy as np
#import matplotib.pyplot as plt

x=np.linspace(0,2*np.pi,11)
y=np.sin(x)

for i in range(0,11):
  print("(%.2f,%.2f)" % (x[i],y[i]))
