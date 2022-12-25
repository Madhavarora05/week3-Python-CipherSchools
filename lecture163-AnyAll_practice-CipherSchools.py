def msum(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "Wrong Output"
print(msum(1,2,3,4,8,9))