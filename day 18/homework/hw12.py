#  12)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტი

num1 = int(input("Enter any number:"))

for i in range(0, num1):
    if i%2!=0:
        print(str(i) + "odd")
    else:
        print(str(i) + "even")