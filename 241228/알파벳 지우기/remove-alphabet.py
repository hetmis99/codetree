a= input()
b=input()
newa, newb=  "", ""

newa= "".join(i for i in a if i.isdigit())
newb= "".join(i for i in b if i.isdigit())
print(int(newa)+int(newb))
