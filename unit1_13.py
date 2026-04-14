from functools import reduce
l=[1,2,3,4]
print(list(map(lambda x:x*2,l)),list(filter(lambda x:x%2==0,l)),reduce(lambda a,b:a+b,l))