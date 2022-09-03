#Program to print prime numbers from 1-200
def PN_Check(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        print(n)
        
for i in range(1,200):
    PN_Check(i)
