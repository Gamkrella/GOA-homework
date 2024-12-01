# დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან 20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში. თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

weight = int(input("Enter your weight"))

if weight>10 and weight<20:
    print("You should get half of a tablet once a day")
elif weight>30 and weight<40:
    print("You should get one tablet twice a day")
elif weight>45:
    print("You should get 3 tablets twice a day")
    