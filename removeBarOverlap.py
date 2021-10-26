import numpy as np
from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexs = np.arange(len(ages_x))

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexs-0.25,dev_y, width = 0.25,color = "#012e56", label = "All devs")
plt.bar(x_indexs,py_dev_y, width = 0.25,color = "c", label = "Python")
plt.bar(x_indexs+0.25,js_dev_y, width = 0.25, color = "r",label = "JavaScript")

plt.xticks(ticks=x_indexs, labels=ages_x)

plt.legend()
plt.show()