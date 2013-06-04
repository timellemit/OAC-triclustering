import random

user_len = 20
tag_len = 20
res_len = 20
triples_num = 5000 # approximately
density = pow(float(triples_num)/user_len/tag_len/res_len, 1./3)
user_tag_density = density
user_res_density = density
tag_res_density = density

f = open('input/context_gen5_' + str(user_len) +'x' + str(tag_len) + 'x' + str(res_len) + '.txt','w')
f.write(str(user_len) + ',' + str(tag_len) + ',' + str(res_len) + '\n')

def gen_users_tags_resources_names():
    users, tags, resources = '', '', ''
    for i in xrange(user_len):
        users += ('u' + str(i+1) + ',')
    for i in xrange(tag_len):
        tags += ('t' + str(i+1) + ',')
    for i in xrange(res_len):
        resources += ('r' + str(i+1) + ',')
    f.write(users.rstrip(',') + '\n')
    f.write(tags.rstrip(',') + '\n')
    f.write(resources.rstrip(',') + '\n')
    return

def gen_u_t_matrix():
    for i in xrange(user_len):
        a = ''
        for j in xrange(tag_len):  
            a += ('0' if random.random() > user_tag_density else '1')
        f.write(a+'\n')
    return

def gen_u_r_matrix():
    for i in xrange(user_len):
        a = ''
        for j in xrange(res_len):
            a += ('0' if random.random() > user_res_density else '1')
        f.write(a+'\n')
    return

def gen_t_r_matrix():
    for i in xrange(tag_len):
        a = ''
        for j in xrange(res_len):
            a += ('0' if random.random() > tag_res_density else '1')
        f.write(a+'\n')
    return

gen_users_tags_resources_names()
gen_u_t_matrix()
gen_u_r_matrix()
gen_t_r_matrix()
f.close()

