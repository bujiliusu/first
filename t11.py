from configparser import ConfigParser
import json
cfg = ConfigParser()
readok = cfg.read('test.ini')

d = {}
#print(cfg.sections())
for section in cfg.sections():
    #print(dict(cfg.items(section)))
    d[section]=dict(cfg.items(section))
print(d)

testjson = json.dumps(d)
print(testjson)

# for k,v in cfg.items():
#     print(dict(cfg.items(k)))
#
# testdict = {'a':1, 'b':2}
# print(testdict)
# print(dict(testdict.items()))







