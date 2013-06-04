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
        
    # returns a dictionary of triclusters {hash_key : [user, tag, resource]}
    def triclusters (self, min_density = 0.5, density_check = True):
        Tdict, Tricl = {}, []
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
            else:
                if not Tdict.has_key(Tkey):
                    Tdict[Tkey] = Tricl
            #i+=1
        return Tdict

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
    #context = Context('input\context_large_random.txt')
    context = Context('input\context_3x3x10.txt')
    min_density = 0.2
    # for large input datasets output into output file
    # f = open('output.txt','w')
    Triclusters = context.triclusters(0.7)
    print 'Triclusters: ', Triclusters.values()
    # writing triclusters' list into output file
    #f.write(str(Triclusters))   
    rec_tag_dic, rec_res_dic = context.recommend(Triclusters)
    print 'Recommended tags: ', \
          context.present_rec_tags(rec_tag_dic)
    print 'Recommended resources: ', \
          context.present_rec_resources(rec_res_dic)
