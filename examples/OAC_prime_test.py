import OAC_prime, time

#context = OAC_prime.Context('input\context_gen_1x47x52.txt')
#context = OAC_prime.Context('input\context_gen_1x248x482.txt')
#context = OAC_prime.Context('input\context_gen_1x444x5193.txt')
#context = OAC_prime.Context('input\context_gen_30x30x30.txt')
#context = OAC_prime.Context('input\context_gen_250x795x22.txt')
context = OAC_prime.Context('../input/context_gen_51x924x2844.txt')

print len(context.I), ' triples, denisty = ', float(len(context.I))/\
      context.user_num/context.tag_num/context.res_num

# list for results [(density, exec_time, num_of_tricl)]
param = []
for dens_procent in xrange(0,101,10):
    density = float(dens_procent)/100
    init_time = time.time()
    Triclusters = context.triclusters(density)
    oac_time = round(time.time() - init_time,5)
    n_tricl = len(Triclusters)
    param.append((density, oac_time, n_tricl))

print param
