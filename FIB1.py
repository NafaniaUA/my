fib=[ ]
a=int(input('Vedit pochatok '))
b=int(input('Vvvedit kin '))
i=0
fib1=0
fib2=1
k=0

for i in range (100):
    fib.append(fib1)
    fib1,fib2=fib2,fib1+fib2
  
print(fib)

for f in fib:
    if f>=a and f<=b:
        print(f)



