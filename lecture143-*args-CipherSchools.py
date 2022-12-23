# *args-> helps to add n arguments

def total(*args):
    total=0
    for num in args:
        total+=num
    return total
print(total(1,5,6,3,2))