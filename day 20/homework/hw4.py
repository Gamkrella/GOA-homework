# 5) დაწერეთ ციკლი რომელიც ლუწს გამოიტანს " მე მიყვარს გოა" და კენტს " მე მიყვარს პროგრამირება".

num = int(input("Enter any number: "))
for i in range (0,num):
    if num%2==0:
        print("I love GOA")
    else:
        print("I love programming")