import OAC_prime, time

context = OAC_prime.Context('input\context_gen_30x30x30.txt')

def density(I, X, Y, Z):
    XxYxZ = set([(x,y,z) for x in X for y in Y for z in Z])
    return float(len(set(I) & XxYxZ))/(len(X)*len(Y)*len(Z))

def density2(I, X, Y, Z):
    n = 0
    for x in X:
        for y in Y:
            for z in Z:
                if (x,y,z) in I:
                    n += 1
    return float(n)/((len(X)*len(Y)*len(Z)))

init_time = time.time()
density(context.I,[0,1,4,6,8,12,13,15,16,17],[2,4,5,6,7],[2,3,4,5,7,8,9])
print time.time() - init_time
init_time2 = time.time()
density2(context.I,[0,1,4,6,8,12,13,15,16,17],[2,4,5,6,7],[2,3,4,5,7,8,9])
print time.time() - init_time2
    
