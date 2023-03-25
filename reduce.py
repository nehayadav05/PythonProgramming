from functools import reduce

nums=[3,6,7,9,11]
odds=list(filter(lambda n:n%2!=0,nums))
doubles=list(map(lambda n:n*2,odds))

sum=reduce(lambda a,b:a+b,doubles)

print(sum)