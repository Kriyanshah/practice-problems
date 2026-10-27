# Three lines to make ourr compiler able to draw
import sys
import matplotlib
#matlpotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
x = ["Apples", "Bananas"]
y = [400,320]

plt.bar(x,y)
plt.show()
# Two lines to make our compiler draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()