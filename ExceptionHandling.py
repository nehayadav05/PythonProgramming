a=5
b=0

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Hey,you cannot divide a Number by zero",e)
finally:
    print("resorce closed")