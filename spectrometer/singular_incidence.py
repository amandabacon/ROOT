import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('0_deg.txt')

x = data[:, 0]
y = data[:, 1]

ymax = max(y)
print(ymax)
xpos = np.where(y == ymax)
print(xpos)
xmax = x[xpos]
print(xmax)

text = 'x = %.3f, y = %.3f' % (xmax, ymax)

plt.annotate(text, xy = (xmax, ymax), xytext = (xmax, ymax+5),)

plt.plot(x, y, 'r--')
plt.ylabel('Intensity [counts]')
plt.xlabel('Wavelength [nm]')
plt.savefig('test')
plt.show()
