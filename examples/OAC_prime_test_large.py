import OAC_prime, time

#context = OAC_prime.Context('input\context_gen_1x444x5193.txt')
#context = OAC_prime.Context('input\context_gen_340x14982x61568.txt')
#context = OAC_prime.Context('input\context_gen_59x5823x28920.txt')
context = OAC_prime.Context('../input/context_gen_30x30x30.txt')
#context = OAC_prime.Context('input\context_gen_250x795x22.txt')
#context = OAC_prime.Context('input\context_gen_51x924x2844.txt')

print len(context.I), ' triples, denisty = ', float(len(context.I))/\
      context.user_num/context.tag_num/context.res_num, time.time()

min_density = 0
init_time = time.time()
Triclusters = context.triclusters(density_check = False)
oac_time = round(time.time() - init_time,5)
n_tricl = len(Triclusters)
print oac_time, n_tricl
