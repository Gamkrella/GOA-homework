# გიორგიმ შექმნა ზოოპარკი სადაც შესვლა მხოლოდ კონკრეტული აღნაგობის ხალხს შეუძლიათ. გიორგი ზოოპარკში უშვებს ხალხს რომელიც 180 სანტიმეტრზე მაღლები არიან და 50-90 კილოს შორის არიან წონით. თქვენი მისიაა რომ მომხმარებელს შემოატანინოთ წონა და სიმაღლე და გაარკვიოთ შეუძლია თუ არა მომხმარებელს ზოოპარკის მონახულება.
height = int(input("Enter your height:"))
weight = int(input("Enter your weight:"))

if height>180 and weight>50 and weight<90:
    print("You can enter in my zoo")
else:
    print("You can't enter my zoo")
    