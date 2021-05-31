import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,10]
y = [10.7,10.7,11.4,11.3,11.2,11.2,11,11,11,10.7]
plt.plot(x,y)
plt.xlabel('Beam size')
plt.ylabel('BLEU')
plt.show()