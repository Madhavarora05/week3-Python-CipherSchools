#d={1:"odd",2:"even"}
d={i:('even' if i%2==0 else 'odd') for i in range(1,6)}
print(d)