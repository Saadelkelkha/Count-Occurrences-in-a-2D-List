t = []

for i in range(0, 4):
    l = []
    for j in range(0, 6):
        n = int(input("Type number: "))
        l.append(n)
    t.append(l)

m=int(input("Type the valeur of n :"))

r=0
for i in range(0, 4) :
    for j in range(0, 6):
        if t[i][j]==m :
            r=r+1

if r==0 :
    print(m,"not found in table T")
else :
    print("The number of occurrences of ",m,"in  the table est ",r)
 