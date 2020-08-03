def generator():
    for i in range(10):
        yield i+1
        


k=generator()
#k.throw(TypeError,'FOO') з цим не працює пише що неспівпадіння типів
print(next(k))


l=[1,3,4,5,6,7]
b = l.__iter__() 

print(b.__next__())
print(b.__next__())
print(b.__next__())
