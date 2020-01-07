l= ['hi','bye','howru']
c = []
def longone(l):
    for i in l:
        c.append(len(i))
        temp = c.index(max(c))
    print(l[temp])
i = longone(l)