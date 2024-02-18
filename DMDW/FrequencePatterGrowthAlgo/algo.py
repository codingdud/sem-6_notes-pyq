
data = [
    {'K': 1, 'E': 1, 'M': 1, 'O': 1, 'Y': 1},
    {'K': 1, 'E': 1, 'O': 1, 'Y': 1},
    {'K': 1, 'E': 1, 'M': 1},
    {'K': 1, 'M': 1, 'Y': 1},
    {'K': 1, 'E': 1, 'O': 1,'Y':1},
]
itemCount={'K':0, 'E':0, 'M':0, 'O':0, 'Y':0}
for i in data:
    for j in i:
        itemCount[j]=i[j]+itemCount[j]
print(itemCount)

suport={'K':0, 'E':0, 'M':0, 'O':0, 'Y':0}
for d in itemCount:
    suport[d]=itemCount[d]/len(itemCount)
print(suport)

supthres=[]
treshold=0.6
for i in suport:
    supthres.append(1 if suport[i]>treshold else i)
print(supthres)

fre=[]
for i in data:
    temp={}
    for j in i:
        if(suport[j]>treshold):
            temp[j]=1
    fre.append(temp)
for i in data:
    print(i)
print()
for i in fre:
    print(i)

tree={}
for i in fre:
    main=tree
    for j in i:
        if j not in main.keys():
            main[j] ={'val':1}
            main=main[j]
        else:
            main[j]['val']+=1
            main=main[j]

print(tree)