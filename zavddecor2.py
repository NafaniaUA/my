l={}

def my_decorator(func):
    def wrapper(n):
        #print("До роботи функції.")
        result=func(n)
        
        l[n]=result
        print(n)
        #print("Після роботи функції.")
        return result
    return wrapper

@my_decorator
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

l1 = fibonacci(10)

    
print(l)    


