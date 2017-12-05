#function to plot f(x) = sin^2(x-2)e^-(x^2)
import numpy as nump
import matplotlib.pylab as py

x = nump.linspace(0,2)
y1 = nump.sin(x-2)**2
y2 = nump.exp(-(x**2))
y = y1*y2
py.plot(x,y,'k--')
py.xlabel('Interval')
py.ylabel('Function - f(x)')
py.title('Ploting a function using \'matplotlib\'')
py.show()