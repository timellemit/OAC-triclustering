from itertools import product

class Context:
    def __init__(self, input_context):
        self.user_num, self.tag_num, self.res_num, \
        self.U, self.T, self.R, self.I = \
        input_context
        
    def r_prime(self, u, t):
        prime = []
        for (g, m, b) in self.I:
            if g == u and m == t:
                prime.append(b)
        return prime
    
    def t_prime(self, u, r):
        prime = []
        for (g, m, b) in self.I:
            if g == u and b == r:
                prime.append(m)
        return prime
    
    def u_prime(self, t, r):
        prime = []
        for (g, m, b) in self.I:
            if m == t and b == r:
                prime.append(g)
        return prime
    
    def density(self, X, Y, Z):
        XxYxZ = set([(x,y,z) for x in X for y in Y for z in Z])
        return float(len(set(self.I) & XxYxZ))/(len(X)*len(Y)*len(Z))
    
    # returns the number of triconcepts in a tricluster (A,B,C)
    def triconcept_num(self, tricl):
        X, Y, Z = tricl[0], tricl[1], tricl[2]
        XxYxZ = set([(x,y,z) for x in X for y in Y for z in Z])
        return float(len(set(self.I) & XxYxZ))
         
    # returns a dictionary of triclusters {hash_key : [user, tag, resource]}
    def triclusters (self, min_density = 0.5, density_check = True):
        Tdict, Tricl, dens_tricl_list = {}, [], []
        #i, len_I = 0.,len(self.I)
        for (g, m , b) in self.I:
            #writing current process into output file 
            #f.write(str(round(100*(i+1)/len_I),2) + '%\n')
            Tricl = self.u_prime(m, b), self.t_prime(g, b), self.r_prime(g, m)
            Tkey = hash(str(Tricl))
            if density_check:
                dens = self.density(Tricl[0], Tricl[1], Tricl[2])
                if not Tdict.has_key(Tkey) and dens >= min_density:
                    Tdict[Tkey] = Tricl
                    dens_tricl_list.append((dens, Tricl))
            else:
                if not Tdict.has_key(Tkey):
                    Tdict[Tkey] = Tricl
                    dens_tricl_list.append((dens, Tricl))
            dens_tricl_list.sort(reverse = True)
        return Tdict, dens_tricl_list
    
    def list_triconcepts(self, user, tag): 
        triconc_list = []
        for triconc in self.I:
            if user == triconc[0] and tag == triconc[1]:
                triconc_list.append(triconc)
        return triconc_list
    
    def list_triclusters(self, user, tag, Tdict): 
        tricl_list = []
        for tricl in Tdict.values():
            if user in tricl[0] and tag in tricl[1]:
                tricl_list.append(tricl)
        return tricl_list
    
    def sort_tricl_by_size(self, Tdict):
        size_tricl_list = []
        for tricl in Tdict.values():
            square = len(tricl[0])*len(tricl[1])
            size_tricl_list.append((square,tricl))
        size_tricl_list.sort(reverse = True)
        return size_tricl_list
    
    # returns a list of triclusters including (user, tag) sorted by included amount of triconcepts
    def list_tricls_by_triconcepts(self, user, tag, Tdict): 
        tricl_list = []
        for tricl in Tdict.values():
            if user in tricl[0] and tag in tricl[1]:
                measure = self.triconcept_num(tricl)
                tricl_list.append((measure, tricl))
        tricl_list.sort(reverse = True)
        return tricl_list
        
    def biggest_tricl(self, user, tag, Tdict):  
        tricl_list = []
        for tricl in Tdict.values():
            if user in tricl[0] and tag in tricl[1]:
                measure = self.triconcept_num(tricl)
                tricl_list.append((measure, tricl))
        tricl_list.sort(reverse = True)
        return tricl_list[0][1]            
    # returns 2 dictinaries: {user : [recommended_tags]}
    #                  and   {user : [recommended_resources]}
    def recommend(self, Tdict):
        Res, Tag = {}, {}
        def tags(self, user):
            return [t for (u,t,r) in self.I if u == user]
        def resources(self, user):
            return [r for (u,t,r) in self.I if u == user]
        def tags_tricl(user, tricl):
            return tricl[1] if user in tricl[0] else []
        def resources_tricl(user, tricl):
            return tricl[2] if user in tricl[0] else []
        def sim(self, user, tricl):
            Tu = set(tags(self, user))
            Ru = set(resources(self, user))
            Ttricl = set(tags_tricl(user, tricl))
            Rtricl = set(resources_tricl(user, tricl))
            sim = 0.5*(float(len(Ru & Rtricl))/len(Ru | Rtricl) + \
                        float(len(Tu & Ttricl))/len(Tu | Ttricl))
            return sim
        def sims(self, user):
            sims = {}
            for Tkey in Tdict.keys():
                similarity = sim(self, user, Tdict[Tkey])
                if similarity not in sims.keys():
                    sims[similarity] = []
                sims[similarity].append(Tkey)
            return sims
        def rec_tags(self, user, sims):
            sims_keys = sims.keys()
            sims_keys.sort(reverse = True)
            for similarity in sims_keys:
                for tricl_key in sims[similarity]:
                    Tag[user] = list(set(tags_tricl(user, Tdict[tricl_key])) \
                    - set(tags(self, user)))
                    if len(Tag[user]) > 0:
                        return 
        def rec_resources(self, user, sims):
            sims_keys = sims.keys()
            sims_keys.sort(reverse = True)
            for similarity in sims_keys:
                for tricl_key in sims[similarity]:
                    Res[user] = list(set(\
                        resources_tricl(user, Tdict[tricl_key])) - \
                                     set(resources(self, user)))
                    if len(Res[user]) > 0:
                        return 
        for user in xrange(len(self.U)):
            sim_dic = sims(self, user)
            rec_tags(self, user, sim_dic)
            rec_resources(self, user, sim_dic)
          
        return Tag, Res
    
    # return the same tricluster with names not numbers
    def present_tricl(self, tricl):
        print self.U
        new_tricl = [([self.U[u] for u in tricl[0]], [self.T[t] for t in tricl[1]], \
                       [self.R[r] for r in tricl[2]])]
        return new_tricl
    
    # retrurns the same array of triclusters but with user, tag and resources names
    def present_triclusters(self, Tricls):
        new_tricls = [self.present_tricl(tricl) for tricl in Tricls]
        return new_tricls
    # returns the same dictionary but with user \
    # and tags names, not numbers
    def present_rec_tags(self, rec_tag_dic):
        rec_tags = [(self.U[u], [self.T[t] for t in tags]) \
                    for (u, tags) in rec_tag_dic.items()]
        return rec_tags

    # returns the same dictionary but with user \
    # and resources names, not numbers
    def present_rec_resources(self, rec_res_dic):
        rec_res = [(self.U[u], [self.R[r] for r in ress]) \
           for (u, ress) in rec_res_dic.items()]
        return rec_res

if __name__ == '__main__':
    from parse_input import *
    #context = Context('input\context_large_random.txt')
    context = Context(parse_input(open('input/context_3x4x5.txt', 'rt')))
    min_density = 0.2
    # for large input datasets output into output file
    # f = open('output.txt','w')
    Triclusters, dens_tricl_list = context.triclusters(0.7)
    print 'Triclusters: ', Triclusters.values()
    print 'New tricls', context.present_triclusters(Triclusters.values())
    # writing triclusters' list into output file
    #f.write(str(Triclusters))   
    print 'sort_tricl_by_size',context.sort_tricl_by_size(Triclusters)
    print 'list_tricl_by_concepts', context.list_tricls_by_triconcepts(2,2, Triclusters)
    rec_tag_dic, rec_res_dic = context.recommend(Triclusters)
    print 'Recommended tags: ', \
          context.present_rec_tags(rec_tag_dic)
    print 'Recommended resources: ', \
          context.present_rec_resources(rec_res_dic)
    context2 = Context(parse_input(open('input/context_gen_20x20x200.txt', 'rt')))
    min_density = 0.2    
    tricl = [[3, 5, 14, 18], [1, 3, 8, 19], [9, 16, 28, 35, 66, 71, 74, 75, 78, 82, 89, 128, 133, 144, 162, 188]]
    print context2.present_tricl(tricl)