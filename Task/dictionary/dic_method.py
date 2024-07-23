watch_details= {
     'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Cartier':8000
}
#keys()- return a list containing the dictionary keys
key = watch_details.keys()
print('key:',key)

#value()
value = watch_details.values()
print('value:',value)

#get()
get = watch_details.get('Titan')
print('get:',get)

#items
items = watch_details.items()
print('item:',items)

#update()
watch_details.update({'Noise':12000})
print('update:',watch_details)

#pop()
watch_details.pop('Titan')
print('pop:',watch_details)