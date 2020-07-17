import random
print('Гра починається:) Введіть числа яки знаходяться в діапазоні від 0 до 20')
while True:
    a=int(input('Ведіть початок діапазону чисел для вгадування '))
    b=int(input('Введіть кінець діапазону для вгадування '))
    if a<b and a!=b and a>=0 and b<=20:
        break
    else:
          print('Введіть числа в діапазоні від 0 до 20 і зважайте що a<b')
CH=random.randint(a,b)
#print(CH)
print('Гра почалась :)')
while True:
    a=int(input('Введіть число '))
    if a < CH:
        print('Ви ввели число яке меньше заданого ')
        print('Спробуйте ще раз ')
    elif a > CH:
         print('Ви ввели число яке більше заданого ')
         print('Спробуйте ще раз ')
    elif a==CH:
        print('Ви виграли!!!')
        print('Загадане число ',CH)
        break