from pathlib import *
p = Path('a/b/c')
print(len(p.parents))
print(p.parents)
print(list(p.glob('*,log')))

f=Path('d:/test.txt').open('r+')
print(type(f))
with f:
    f.write('abc')