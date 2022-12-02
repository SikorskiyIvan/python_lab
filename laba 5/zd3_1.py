from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
x = 12.1
c = np.arange(-10, 1)
print('C:', c)
a = np.around(2*x - c)
a_abs = np.abs(a)
a_abs_3 = np.power(a_abs, 3)
l = np.power(a_abs_3, 1/5) + 0.567
l.sort()
print('L:', l)
print(f'the maximum value is: {l[-1]}')
print(f'the minimum value is: {l[1]}')
print(f'average value f(x) is: {mean(l)}')
f = np.arange(0, 8.09734630737339, 0.5)
print('F:', f)
y = f
plt.plot(c, l)
plt.plot(f, y)
plt.title("График функции и прямой")
plt.show()



