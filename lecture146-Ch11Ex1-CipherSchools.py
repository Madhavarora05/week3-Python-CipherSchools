def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"
num=[1,2,3]
x=int(input("Enter power number: "))
print(power(x,*num))