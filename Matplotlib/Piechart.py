# Three lines to make ourr compiler able to draw
import sys
import matplotlib
#matlpotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

y = np.array([35,25,25,15])

plt.pie(y)
plt.show()

# Two lines to make our compiler draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()