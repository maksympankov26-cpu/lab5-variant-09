import math
from typing import Callable
def solve_method(func:Callable[[float],float],x0:float,eps:float):
    y=func(x0)
    print(y)
def func(x0):
    return math.cos(x0**2)-x0*10
x0=1.0
eps=0.00002
solve_method(func,x0,eps)