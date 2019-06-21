



# find out isprime
def isprime(i):
    q=0
    for u in range(1,i+1):
        if i%u==0:
            q+=1
            #print(u)
    if q==2:
        return True
    else:
        return False

# find out how many char & digits in a given string

u=input()
s=[]
c=0
dc=0
up=0
l=0
for i in u:
    if i.isalpha():
        if i.isupper():
            up+=1
        elif i.islower():
            l+=1
    elif i.isdigit():
            dc+=1
print(dc,l,up)