# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
TotalMoney = 1000
quantity = 3
price = 450
print(f"I have {TotalMoney}$ . So i want buy {quantity} balls to {price}$ ")

olma=int(input("olma soni : "))
bola = int(input("bola soni : "))
qoldiq = olma % bola
son = (olma - qoldiq )/bola
print("harbir bola ",int(son),"olma oladi",qoldiq,"olma qoladi")


son = int(input("son kiriting "))
summary = int(son*(son-1)/2)
print("natija ",summary)


yil = int(input("yilni kiriting: "))
a = yil % 19
b = yil // 100
c = yil % 100
d = b // 4
e = b % 4
f = b + 825
g = b - f + 13
h = (19 * a + b - d - g +15 ) % 30
i = c // 4
k=c % 4
l =( 32 + 2 * e + 2 * i - h - k ) % 7
m = (a + 11 * h + 22 * l) // 451
oy = (h + l + 7 * m + 114 ) // 31
sana = (h + l - 7 * m + 114) % 31 
print("paxsa kuni sanasi: "+str(sana)+"."+str(oy)+"."+str(yil))


cars =['gm','tayota','bugatti','lamborghini','nexia','bmw']
for element in cars:
    if element!='gm' and element != 'bmw':
        print(element.title())
    else:
        print(element.upper())

ism = input("o'zingizni tanishtiring : ")
if ism.lower() == 'admin':
    print("Hush kelibsiz,Admin!\nMijozlar ro'yxatini ko'rmoqchimisiz?")
else:
    print(f"Hush kelibsiz {ism}")
 
ason = int(input("a= "))
if ason >= 0:
    print("ushbu son musbat")
else:
    print("ushbu son manfiy")


a=float(input("son kiriting: "))
if a>=0:
    print("ushbu sonning ildizi",pow(a, 1/2))
else:
    print("musbat son kiriting")

son = int(input("Juft son kiriting "))
if son%2==0:
    print("raxmat")
else :
    print("bu son juft emas")
    
yosh = int(input("yoshizni kiriting "))
if yosh <=4 or yosh >= 60:
    narh = 0
elif yosh<18:
    narh = 10000
else:
    narh = 20000
print(narh)


a= int(input("birinchi sonni kiriting: "))
b= int(input("ikkinchi sonni kiriting: "))
if a>b:
    print(a,">",b)
elif a==b:
    print(a,"=",b)
else:
    print(a,"<",b)
    


a=float(input())
if(a>=0 and a<=2):
    b=a*10.5
elif(a>2):
    b=21+(a-2)*4
else:
    b="yil manfiy bulmaydi"
    
print(b)
'''
suzlar={"float":"haqiqiy son","integer":"butun son","if-else":"shart operatori","string":"satr","bool":"mantiqiy operator","array":"massiv","insert":"kiritish komandasi","max":"eng katta elementi","print":"chop etish"}
a=input().lower()
suz=suzlar.get(a,"bunday qiymat mavjud emas")
print(suz)
    