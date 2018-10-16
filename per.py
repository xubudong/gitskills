import numpy as np
import matplotlib.pyplot as  plt
  
x,y = np.loadtxt('data.txt',unpack=True)
plt.plot(x,y)
plt.show()
