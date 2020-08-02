
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f'Call {func.__name__} with args:{args}, kwargs: {kwargs}'
        )
        result = func(*args,**kwargs)
        return result
    return wrapper

@logged
def func(*args):
    #print(len(args))
    return 3 + len(args)       

@logged
def func(**kwargs):
    #print(len(args))
    return 3 + len(kwargs)       

res=func(k1=4, k2=4, k3=4) 
print(res)