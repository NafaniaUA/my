import math
print ('Для обчислення факторіалу ведіть діапазон додатніх чисел та крок який быльше нуля')
while True:
    a=int(input('Введіть початок діапазону визначення факторіалу '))
    b=int(input('Введіть кынець дыапазону визначення факторіалу'))
    c=int(input('Введіть крок'))
    if a>=0 and b>=0 and a<b and c>0:
        break
    else:
        print('Введіть коректні дані')

fact=a
for fact in range(a,b+1,c):
    print(math.factorial(fact))
    

