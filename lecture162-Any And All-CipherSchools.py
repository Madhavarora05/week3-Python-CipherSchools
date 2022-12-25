num1=[2,4,6,8,10]
num2=[1,2,3,5,7,9]
num3=[2,3,4,5,6]
x=all([num%2==0 for num in num1])
y=all([num%2==0 for num in num3])
z=any([num%2==0 for num in num2])
print(x)
print(y)
print(z)