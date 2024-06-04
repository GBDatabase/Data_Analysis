mydict = {'kim' :1111,'park' : 2222,'lee' : 3333}
ketlist = mydict.keys()

for i in ketlist:
    print(i)
    print(mydict[i])

valuelist = mydict.values()
for i in valuelist:
    print(i)

#items()
for item in mydict.items():
    print(item)
    print(item[0])
    print(item[1])