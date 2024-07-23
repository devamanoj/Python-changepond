student_id = {11,12,13,14}
print('set:',student_id)
mixed = {'deva',123,132,True,245}
print('set1:',mixed)
print('length:',len(mixed))

s1={True,0,1,False}
print(s1)
s1={True,1}
print(s1)

#task1 -iterate using for loop
mixeds = {'subham',25,124,True,124}
for item in mixeds:
    print(mixeds)

#set methods
#insert,update,delete
mixeds = {'subham',25,True,124}

#add()-add elements to the set
mixeds.add('trainer')
print('add:',mixeds)

#update()
update = {12567,5678}
mixeds.update(update)
print('updateMethod:',mixeds)

#discard()

mixeds.discard('trainer')
print('discard:',mixeds)

mixeds.remove(5678)
print('remove:',mixeds)