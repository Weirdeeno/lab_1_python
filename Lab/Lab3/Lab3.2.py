'''
12. Дано дійсне число - ціна 1 кг цукерок. Вивести вартість 1, 2, ..., 10 кг цукерок.
'''



c = int(input("Введите стоимость конфет за 1 кг : "))
x = 1
while x <= 10:

   print("Цена за %.0f кг конфет - %.1f"%(x, c * x))
   x += 1