import matplotlib.pyplot as plt
import math as mt




def polyx(n):
    return mt.sin((3*mt.pi*n) / 100)


def polyy(n):
    if n==0:
        return ((-1.5*polyx(n))+(2*polyx(n+1))-(0.5*polyx(n+2)))
    elif n>0 and n<=198:
        return ((0.5*polyx(n+1))-(0.5*polyx(n-1)))
    elif n==199:
        return ((1.5*polyx(n))-(2*polyx(n-1))+(0.5*polyx(n-2)))




listn = list(range(200))
x = [polyx(n) for n in listn]
y = [polyy(n) for n in listn]



plt.plot(listn, x, '#FF2079', label = 'Value of x(n)')
plt.plot(listn, y, '#440BD4',label = 'Value of y(n)')
plt.legend()
plt.show()