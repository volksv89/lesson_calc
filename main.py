# Дурацкий калькулятор
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.CYAN)
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

operation = input("Что сделать? (+/-)")
result = 0

if operation =="+":
    result = a + b
elif operation == "-":
    result = (a - b)

# Так же можно продолжить с * и /
print(Fore.YELLOW)
print(f"Результат {result}")
