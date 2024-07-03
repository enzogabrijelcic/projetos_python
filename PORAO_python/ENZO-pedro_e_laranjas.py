print ("pedro tem 10 laranjas.")
v = int(input("quantas laranjas voce tirou de Pedro?"))
f = 10 - int (v)
if f > v:
    print ("Pedro ficou com",f, ",ele está feliz")
elif f == v:
    print ("Pedro ficou com",f, ",ele está feliz")
else:
    print ("Pedro ficou com",f, ",ele está triste")
