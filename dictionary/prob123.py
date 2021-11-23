#supermarket
d={'store1':{'name':'durga','item':[{'name':'soap','qt':20},{'name':'brush','qt':30}]},

            'store2':{'name':'laxmi','item':[{'name':'flour','qt':40},{'name':'rice','qt':10}]}}

print(d['store1']['name'])
print(d['store2']['name'])


for s in d['store1']['item']:
    print(s['name'])

for s in d['store2']['item']:
    if s['name']=='rice':
        print("value is",s['qt'])
print("the value of rice is",d['store2']['item'][1]['qt'] )