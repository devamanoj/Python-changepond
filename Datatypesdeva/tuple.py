# #create a tuple
# #homogeneous
# student_id = (123,124,125,125)
# ice_cream = ('vanilla','choclate chips','blueberry')

# #heterogeneous
# mixed = (123,'hello',False,56.78)
# print(len(mixed))
# ice_creame = ('Vanilla')        # str
# print(ice_creame,type(ice_creame))
# ice_creame = ('Vanilla',)       # comma (tuple)
# print(ice_creame,type(ice_creame))

# # immutable
# mixed[0] = True
# print("False ",mixed)
ice_cream = ('vanilla','choclate chips','blueberry')
countmethod = ice_cream.count('vanilla')
print('count method:',countmethod)
print()
Index_method = ice_cream.index('vanilla')
print('Index method:',Index_method)

