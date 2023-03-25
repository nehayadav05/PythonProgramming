nums=[9,7,4,5,3,2]
odds=list(filter(lambda n:n%2!=0,nums))
doubles=list(map(lambda n:n*2,odds))
print(doubles)