'''
Лабораторна робота №5
Функції та декомпозиція задач
Панков Максим
Студент групи №2
Номер варіанта: 9
'''
import math
from typing import Callable
def newton_method(func:Callable[[float],float], df:Callable[[float],float], x0:float, eps:float):
    x1 = x0 - func(x0)/df(x0)
    while abs(x1-x0) >= eps:
        x0 = x1
        x1 = x0 - func(x0)/df(x0)
    return x1
def func(x0):
    return math.cos(x0**2)-x0*10
def df(x0):
    return -2*x0*math.sin(x0**2)-10
x0=2
eps=0.00002
print(newton_method(func, df, x0, eps))