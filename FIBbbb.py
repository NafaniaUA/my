fib=[ ]
fib1=0
fib2=1
с=0

for i in range(20):
    fib.append(fib1)
    fib1,fib2=fib2,fib1+fib2
    
while True:
    k=int(input('Vvedit chislo '))
    
    if k in fib:
         print('Zadacha ocinena na ',k,' baliv')
         break
    else:
        print('vvedit kor chislo')
           
print(fib)

