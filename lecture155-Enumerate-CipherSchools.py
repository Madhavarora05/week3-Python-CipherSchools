names=['abc','abcdef','madhav']
#print 0--->abc
#1----->abcdef using enumerate

for pos,name in enumerate(names):
    print(f"{pos}---->{name}")