products = [
    {'p_id':101,'p_name':'Apple','p_price':56000,'p_color':'white'},
    {'p_id':102,'p_name':'Samsung','p_price':46000,'p_color':'silver'},
    {'p_id':103,'p_name':'Vivo','p_price':25000,'p_color':'white'},
    {'p_id':104,'p_name':'Apple','p_price':65000,'p_color':'golden'},
    {'p_id':105,'p_name':'Vivo','p_price':20000,'p_color':'black'},
    {'p_id':106,'p_name':'Samsung','p_price':50000,'p_color':'black'},
    {'p_id':107,'p_name':'Samsung','p_price':60000,'p_color':'white'},
    {'p_id':108,'p_name':'Apple','p_price':80000,'p_color':'silver'}
]

'''
for p in products:
    #print(p)
    if p['p_name'] == 'Apple':
        print(p)
'''
for p in products:
    if p['p_price'] < 30000:
        print(p)
