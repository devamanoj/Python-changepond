# menu_card=['panner','Dal','rice']
# print('avaliable items',menu_card)
# #append()--> adds an element at the end of the list 
# menu_card.append('kofta')
# print('after append method avaliable items',menu_card)

# #extend() --> add the elements of the list to the end of the list
# menu_card.extend(['dal tadaka','biriyani'])
# print("using extend method",menu_card)
# #insert()--> add an element at specified positions
# menu_card.insert(1,'VegBiriyani')
# print('Using Insert method:',menu_card)

# #remove()--> will remove specified value
# menu_card.remove('Dal')
# print('Using Remove Mothod',menu_card)

# #pop()--> wil remove specied index
# menu_card.pop(2)
# print('using the method:',menu_card)

menu_card = ['Panner','Biriyani','Dosa','Panner']
#Index method

Index_method = menu_card.index('Dosa')
print('It will give the position : ',Index_method)

Index_method = menu_card.index('Panner')
print('It will give the position : ',Index_method)

# sort method
menu_card.sort()
print('sort position :',menu_card)
