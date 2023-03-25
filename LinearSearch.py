pos=-1
def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
        
    return False

list=[6,67,4,8,3]
n=3
if search(list,n):
    print("Found at",pos)
else:
    print("Not found")    