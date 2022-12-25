l1=[1,3,5,7]
l2=[2,4,6,8]
print(list(zip(l1,l2)))


l=[(1,2),(3,4),(5,6),(7,8)]
l3,l4=list(zip(*l))
print(l3,l4)
