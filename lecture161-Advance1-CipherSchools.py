#define a function take any no.of lists
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+4+7)/3 (2,5,8)/3 (3,6,9)/3
#solve this in minimum possible lines

# def avg(*args):
#     avg=[]
#     for i in zip(*args):
#         avg.append(sum(i)//len(i))
#     return avg

avg=lambda *args:[sum(i)//len(i) for i in zip(*args)]
print(avg([1,2,3],[4,5,6],[7,8,9]))
