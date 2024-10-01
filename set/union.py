# To union two or more sets using set.union()

s1 = {'A','B'}
s2 = {'C','D'}

print(set.union(s1,s2))
print('----------------')
print(s1.union(s2))
print('----------------')

# To union two or sets using Pipe operator

s3 = {'E'}

print(s1 | s2 | s3)

# Difference between union and '|'

l1 = [1,2,3,4,5,5]
t1 = ('Tim','Tom','Tom')

print(set.union(s1,s2,s3,l1,t1)) # union method convert iterables like list or tuple to their set counterpart and then perform union

print(s1|s2|s3|l1|t1) # {Pipe operator allows only union of set}




