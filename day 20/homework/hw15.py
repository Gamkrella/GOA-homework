# 16)შეიყვანეთ რიცხვი და დაბეჭდეთ მისი ყველა წყვილი რიცხვი (მაგალითად, 8 -> 2, 4, 6, 8)
a=int(input("num"))

if a%2!=0:
    a=a-1

while a>0:
    print(a)
    a=a-2