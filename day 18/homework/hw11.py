# / 11) მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ მხოლოდ კენტი რიცხვები

num1 = int(input("Enter any number:"))

for i in range(0, num1):
    if i%2!=0:
        print(i)