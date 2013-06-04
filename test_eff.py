from time import time
from OAC_prime import Context

times1, times2 = [], []
for adr in ['input/context_gen_20x20x20.txt',\
'input/context_gen2_20x20x20.txt',\
'input/context_gen3_20x20x20.txt',\
'input/context_gen4_20x20x20.txt',\
'input/context_gen5_20x20x20.txt']:
    context1 = Context(adr)
    context2 = Context(adr)
#     init_time = time()
#     tricl1 = context1.triclusters(0, True)
#     times1.append(time() - init_time)
    init_time = time()
    tricl2 = context1.triclusters2(0, True)
    times2.append(time() - init_time)
print times1, times2

