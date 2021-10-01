# Programmers: Hannah & Gabriel
# Course: CS151, Prof. Mehri
# Date: 10/02/21
# Lab Number: 03
# Program Inputs: Weight of package and distance the package is sent.
# Program Outputs: Cost of shipping

wieght = float(input("Enter a weight in kg: "))
distance_miles = float(input("Enter distance in miles: "))


if distance_miles < 10 or distance_miles > 3000:
    print("Error, distance is out of range!")

else:
        if wieght <= 2:
            price = ((distance_miles / 500) * 1.10)
            print("Shipping price: ", price)

        else:
            if wieght > 2 and wieght <= 6:
                price = ((distance_miles / 500) * 2.20)
                print("Shipping price: ", price)

            else:
                if wieght > 6 and wieght <= 10:
                    price = ((distance_miles / 500) * 3.70)
                    print("Shipping price: ", price)

                else:
                    if wieght > 10 and wieght <= 20:
                        price = ((distance_miles / 500) * 4.80)
                        print("Shipping price: ", price)

                    else:
                        if wieght > 20:
                            print("Error, wieght is out of range!")

