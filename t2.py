def check():
    a=[1,2,3]
    print(id(a))
    return a
b= check()
b.append(4)
print(b)

c= check()
print(c)

from functools import wraps
@wraps(check())
def check2():
    a=[1,2,3]
    print(id(a))
    return a