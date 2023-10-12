import os
import time
import turtle
from turtle import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources["money"] = 0


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == 'report':
            print(f" Water : {resources['water']}ml")
            print(f" Milk : {resources['milk']}ml")
            print(f" Coffee : {resources['coffee']}g")
            print(f" Money : ${resources['money']}")

        elif choice == 'Off':
            print("Turning off.")
            exit()

        elif choice in MENU:
            drink_info = MENU[choice]
            water_supply = (drink_info['ingredients']["water"])
            milk_supply = (drink_info['ingredients']['milk'])
            coffee_supply = (drink_info['ingredients']['coffee'])
            resource_water = (resources['water'])
            resource_milk = (resources['milk'])
            resources_coffee = (resources['coffee'])

            if water_supply <= resource_water and coffee_supply <= resources_coffee and milk_supply <= resource_milk:
                print("Please, proceed with the payment.")
                penny = int(input("How many pennies?"))
                nickel = int(input("How many nickels?"))
                dime = int(input("How many dimes?"))
                quarter = int(input("How many quarters?"))
                total = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny
                if total > drink_info['cost']:
                    resources['money'] -= drink_info['cost']
                    resources['coffee'] -= coffee_supply
                    resources['milk'] -= milk_supply
                    resources['water'] -= water_supply
                    balance = total - drink_info['cost']
                    print(f"Here is your balance ${balance: 0.2f}.")
                    print("Enjoy you drink.")
                else:
                    print("Insufficient amount.")
            elif water_supply > resource_water:
                print("Not enough water.")
            elif milk_supply > resource_milk:
                print("Not enough milk.")
            elif coffee_supply > resources_coffee:
                print("Not enough coffee.")
        main_page = (input("Would you like to go to the main page? :")).lower()
        if main_page != 'yes':
            break

coffee_machine()