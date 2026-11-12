'''
Лабораторна робота №5
Функції та декомпозиція задач
Панков Максим
Студент групи №2
Номер варіанта: 9
'''
import math
from typing import Callable
def main(): # початок функції main()
    def save_results_to_file(i:int,x1:float,A:list): # розпис функції для збереження результатів у файл
        with open('results_variant_09.txt', 'w', encoding='utf-8') as file:
            for j in range (i+1):
                file.write(f'Результати {j}-го обчислення : {A[j]}\n')
            file.write(f'Підсумковий корінь: {x1:.6f}\n')
    def newton_method(func:Callable[[float],float], df:Callable[[float],float], x0:float, eps:float,a:float,b:float): #розпис функції активатора методу Ньютона
        x1 = x0 - func(x0)/df(x0)
        i=0
        A=[0 for _ in range(10**7)]
        A[0]=x0
        while abs(x1-x0) >= eps: # цикл, що діє зазначеним чином, який було в умові задачі
            if func(x0)*ddf(x0) <= 0 or x0<a or x0>b: # перевірка умови збіжності методу Ньютона
                return 'Умова збіжності методу Ньютона не виконується, оберіть інше початкове наближення'
            i+=1
            x0 = x1
            x1 = x0 - func(x0)/df(x0)
            A[i]=x1
        save_results_to_file(i,x1,A) # запуск функції зчитки інформації у файл
        return f'За {i} ітерацій було отримано нуль функції (у наближені порядку ε): {x1:.6f}'
    def func(x0:float) -> float: # виклик функції, яка надається в умові задачі
        return math.cos(x0**2)-x0*10
    def df(x0:float) -> float: # виклик похідної функції, яка надається в умові задачі
        return -2*x0*math.sin(x0**2)-10
    def ddf(x0:float) -> float: # виклик другої похідної функції, яка надається в умові задачі
        return -2*math.sin(x0**2)-4*x0**2*math.cos(x0**2)
    x0=float(input('Введіть початкове наближення: '))
    a=-1.35
    b=1.35
    eps=0.00002
    print(newton_method(func, df, x0, eps,a,b)) # вивід результатів роботи функції newton_method
main() # запуск функції main()