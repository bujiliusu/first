# def makekey(s:str):
#     chars = set(r'''!'"#./\{},*-''')
#     key = s.lower()
#     ret = []
#     for i, c in enumerate(key):
#         if c in chars:
#             ret.append(' ')
#         else:
#             ret.append(c)
#     return ''.join(ret).split()

def makekey(s:str):
    chars = set(r"""!'"#./\()[],*- """)
    key = s
    ret = []
    start = 0

    for i, c in enumerate(key):
        if c in chars:
            if start == i:
                start += 1
                continue
            yield key[start:i]
            start = i + 1
    else:
        if start < len(key):
            yield key[start:i]

# test = makekey(r'''abcd...   .###ll''')
# print(test)
# print('*'*40)
d = {}

with open('sample', encoding='utf-8') as  f:
    for line in f:
        #words = line.split()
        for word in makekey(line):
            d[word] = d.get(word, 0) + 1
#print(d)
for k,v in sorted(d.items(), key=lambda item: item[1], reverse=True)[:1]:
    print(k,v)
print(type(sorted(d.items(), key=lambda item: item[1], reverse=True)))