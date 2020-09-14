import logging

FORMAT = "%(asctime)s %(name)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

log1 = logging.getLogger('s')
log1.setLevel(logging.DEBUG)

log2 = logging.getLogger('s.s1')
# print(log2.getEffectiveLevel())
log2.debug('log2 debug')

data = ["{}*{}={}".format(j,i,i*j) for i in range(1,10) for j in range(1,10)]
print(data)