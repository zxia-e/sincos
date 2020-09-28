import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
x2 = np.arange(0, 2*np.pi, 0.1)
y2 = np.cos(x)
#add tan() function
y3 = np.tan(x)

plt.plot(x, y, label = "sin(x)")
plt.plot(x2, y2, label = "cos(x)")
#add tan() function plot
plt.plot(x, y3, label = "tan(x)")
#be sure not to change the y-axis scale from the original project.
plt.ylim(-1.1,1.1)

plt.title("Sine(x) cs. Cos(x)")
plt.legend()

plt.show()