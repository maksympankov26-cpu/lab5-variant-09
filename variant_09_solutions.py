'''
Лабораторна робота №5
Функції та декомпозиція задач
Панков Максим
Студент групи №2
Номер варіанта: 9
'''
import math
from typing import Callable
def main():
    def save_results_to_file(i:int,x1:float,A:list):
        with open('results_variant_09.txt', 'w', encoding='utf-8') as file:
            file.write(f'Підсумковий корінь: {x1:.6f}\n')
            for j in range (i+1):
                file.write(f'Результати {j}-го обчислення : {A[j]}\n')
    def newton_method(func:Callable[[float],float], df:Callable[[float],float], x0:float, eps:float):
        x1 = x0 - func(x0)/df(x0)
        i=0
        A=[0 for _ in range(10**6)]
        A[0]=x0
        while abs(x1-x0) >= eps:
            i+=1
            x0 = x1
            x1 = x0 - func(x0)/df(x0)
            A[i]=x1
        save_results_to_file(i,x1,A)
    def func(x0:float) -> float:
        return math.cos(x0**2)-x0*10
    def df(x0:float) -> float:
        return -2*x0*math.sin(x0**2)-10
    x0=float(input('Введіть початкове наближення: '))
    eps=0.00002
    newton_method(func, df, x0, eps)
main()