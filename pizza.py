import random
import sys
import os
#Gathering Data
def main():
    totalpizzas = 0
    totaltoppings = 0
    sizes = 0
    sizem = 0
    sizel = 0
    basethick = 0
    basethin = 0
    cpepperoni = 0
    cchicken = 0
    ccheese = 0
    cmushrooms = 0
    cspinach = 0
    colives = 0
    

    size = input("Welcome to Ilya's Pizzeria, what size pizza would you like? S, M or L? ")
    base = input("Great, now, what base would you like? Thick or Thin? ")
    pepperoni = input("Would you like Pepperoni on the pizza? Yes or No? ")
    chicken = input("Would you like Chicken on the pizza? Yes or No? ")
    cheese = input("Would you like extra cheese on the pizza? Yes or No? ")
    mushrooms = input("Would you like mushrooms on the pizza? Yes or No? ")
    spinach = input("Would you like spinach on the pizza? Yes or No? ")
    olives = input("Would you like olives on the pizza? Yes or No? ")


    #Verifying whether the inputs are valid
    while size != "S" and size != "M" and size != "L":
        size = input("Please reinput the size, S, M or L. ")
    while base != "Thin" and base != "Thick":
        base = input("Please reinput the base, Thick or Thin? ")
    while pepperoni != "Yes" and pepperoni != "No":
        pepperoni = input("Please reinput, would you like pepperoni? Yes or No? ")
    while chicken != "Yes" and chicken != "No":
        chicken = input("Please reinput, would you like chicken? Yes or No? ")
    while cheese != "Yes" and cheese != "No":
        cheese = input("Please reinput, would you like extra cheese? Yes or No? ")
    while mushrooms != "Yes" and mushrooms != "No":
        mushrooms = input("Please reinput, would you like mushrooms? Yes or No? ")
    while spinach != "Yes" and spinach != "No":
        spinach = input("Please reinput, would you like spinach? Yes or No? ")
    while olives != "Yes" and olives != "No":
        olives = input("Please reinput, would you like olives? Yes or No? ")

    print("Check your order")
    print("Size: ", size)
    print("Base: ", base)
    print("Pepperoni: ", pepperoni)
    print("Chicken: ", chicken)
    print("Extra Cheese: ", cheese)
    print("Mushrooms: ", mushrooms)
    print("Spinach: ", spinach)
    print("Olives: ", olives)

    coi = input("Is that correct? ")
    ordernumber = random.randint(0, 999999)
    if coi == "Yes":
        print("Great! Your order number is:", ordernumber, ". Thank you for calling, your pizza will soon arrive.")
        totalpizzas = totalpizzas + 1
    elif coi == "No":
        print("Oh no! Sorry about that. I'll transfer you back to ordering.")
        main()
    else:
        print("Sorry, I didn't get that. ")
        
    
    if size == "S":
        sizes = sizes + 1
    elif size == "M":
        sizem = sizem + 1
    elif size == "L":
        sizel = sizel + 1
    elif base == "Thick":
        basethick = basethick + 1
    elif base == "Thin":
        basethin = basethin + 1
    elif pepperoni == "Yes":
        cpepperoni = cpepperoni + 1
        totaltoppings = totalpizzas + 1
    elif chicken == "Yes":
        cchicken = cchicken + 1
        totaltoppings = totaltoppings + 1
    elif cheese == "Yes":
        ccheese = ccheese + 1
        totaltoppings = totaltoppings + 1
    elif mushrooms == "Yes":
        cmushrooms = cmushrooms + 1
        totaltoppings = totaltoppings + 1
    elif spinach == "Yes":
        cspinach = cspinach + 1
        totaltoppings = totaltoppings + 1
    elif olives == "Yes":
        colives = colives + 1
        totaltoppings = totaltoppings + 1
    else:
        print(" ")

    percentagepepperoni = totaltoppings % cpepperoni
    percentagechicken = totaltoppings % cchicken
    percentagecheese = totaltoppings % ccheese
    percentagemushrooms = totaltoppings % cmushrooms
    percentagespinach = totaltoppings % cspinach
    percentageolives = totaltoppings % colives
    print("Percentage of chosen pepperoni as an extra topic: ", percentagepepperoni)
    print("Percentage of chosen chicken as an extra topic: ", percentagechicken)
    print("Percentage of chosen extra cheese as an extra topping: ", percentagecheese)
    print("Percentage of chosen mushrooms as an extra topping: ", percentagemushrooms)
    print("Percentage of chosen spinach as an extra topping: ", percentagespinach)
    print("Percentage of chosen olives as an extra topping: ", percentageolives)
main()