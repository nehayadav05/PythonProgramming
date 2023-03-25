pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
         globals()['pos']=mid
         return True
        if list[mid]<n:
         l=mid+1
        else:
         u=mid-1
        
    return False

list=[32,54,23,554,224,44]
n=224
if search(list,n):
    print("Found at",pos+1)
else:
    print("Not found")
