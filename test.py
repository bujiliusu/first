
import inspect
from inspect import Parameter
def add(x:int , y:list) -> str:
    pass

sig = inspect.signature(add)
print(sig)
print(type(sig))
sig2 = sig.parameters
print(sig2)
for i,v in enumerate(sig2.items()):
    print(i,v)
for i,(v,k) in enumerate(sig2.items()):
    print(i,v,k)
    k:Parameter
    print(k.annotation)
    print(k.default)
    print(k.empty)
    print(k.kind)
    print(k.name)
    print(k.POSITIONAL_OR_KEYWORD)
