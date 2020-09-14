# from configparser import ConfigParser
#
# cfg = ConfigParser()
# readok = cfg.read('test.ini')
#print(readok)
#print(type(readok))
#print(type(cfg.sections()))
#print(list(cfg.keys()))

# for setion in cfg.sections():
#     #print(cfg.options(setion))
#     for option in cfg.options(setion):
#         print(option,cfg.get(setion,option))
# print(list(cfg.items()))

# ret = ['1','3','5',' ','abc',' ','cbd']
# print(type(str(ret)))
# print(''.join(ret))

# ret = []
# chars = r'''.,""()'''
# key = 'abcd'
# start = 0
# for i, c in enumerate(key):
#     #print(c)
#     if c in chars:
#         if start == i:
#             start += 1
#             print(start, c)
#             continue
#         ret.append(key[start:i])
#         start = i + 1
#         print(start)
# print(ret)
a = {'a':1, 'b':4, 'c':2}
for k,v in sorted(a.items(), key=lambda item: item[1], reverse=True):
    print(k, v)
for k in a.items():
    print(k)
    print(k[1])



# with open('test.ini') as f:
#     for line in f:
#         words = line.split()
#         # print(line)
#         # print(words)
#     print('__iter__' in dir(f))
