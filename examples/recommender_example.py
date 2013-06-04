import OAC_prime

context = OAC_prime.Context('../input/context_gen_10x10x200.txt')
min_density = 0.2

# returns a dictionary of triclusters {hash_key : [user, tag, resource]}
Triclusters = context.triclusters(min_density)
print 'Triclusters: ', Triclusters.values()

# returns 2 dictinaries: {user : [recommended_tags]}
#                  and   {user : [recommended_resources]}
rec_tag_dic, rec_res_dic = context.recommend(Triclusters)

# print the same dictionary but with user and tags names, not numbers
print 'Recommended tags: ', \
      context.present_rec_tags(rec_tag_dic)
# print the same dictionary but with user and resources names, not numbers
print 'Recommended resources: ', \
      context.present_rec_resources(rec_res_dic)
