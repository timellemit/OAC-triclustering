def parse_input(file):
    context_txt = file
    user_num, tags_num, res_num = [int(s) for s in \
                                   context_txt.readline().strip().split(',')]
    users = context_txt.readline().strip().split(',')
    tags = context_txt.readline().strip().split(',')
    resources = context_txt.readline().strip().split(',')
    matrix = context_txt.readlines()
    ut_matrix = matrix[:user_num]
    ur_matrix = matrix[user_num : 2*user_num]
    tr_matrix = matrix[2*user_num : 2*user_num + tags_num]
    ut_matrix = [[int(s[i:i+1]) for i in xrange(len(s.strip()))] \
                                for s in ut_matrix]
    ur_matrix = [[int(s[i:i+1]) for i in xrange(len(s.strip()))] \
                                for s in ur_matrix]
    tr_matrix = [[int(s[i:i+1]) for i in xrange(len(s.strip()))] \
                                for s in tr_matrix]
    context = []
    for u in xrange(user_num):
        for t in xrange(tags_num):
            for r in xrange(res_num):
                if ut_matrix[u][t]:
                    if ur_matrix[u][r]:
                        if tr_matrix[t][r]:
                            context.append((u,t,r))
                    else:
                        continue
                else:
                    break
                    continue
    return user_num, tags_num, res_num, users, tags, resources, context

        
