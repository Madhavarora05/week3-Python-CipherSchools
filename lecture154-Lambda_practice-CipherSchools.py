#using lambda find even number

x=int(input("Enter number: "))
even=lambda a : a%2==0
print(even(x))

#lambda with if else

#if len(string)>5 return true else false
func=lambda s: True if len(s)>5 else False
print(func('abcde'))