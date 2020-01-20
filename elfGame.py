"""
Program: Elf Game
Description: a probability based game about elves
Author: TwoSails
Version: 1.3.0
"""

import random
import colours as color
import config

version = config.version

print("------ Elf Game ------")

messageOne = 'All the elves sent out died in a horrific gang related incident with goblins. the elves at home are ' \
             'safe and unharmed, no money is made '
messageTwo = 'The elves at home all suffer from food poisoning and vomit to death, ' + color.BRIGHT_GREEN + 'however ' \
                                                                                                     'the elves that were' \
                                                                                                     ' sent out all ' \
                                                                                                     'return home ' \
                                                                                                     'safely with £10 '
messageThree = 'The elves at home are all safe and the elves at work come back with $10 each'
messageFour = 'The elves at home are all safe and the elves at work come back with $20 each'


class Elf:
    def __init__(self):
        self.carryOn = True
        self.roll = 0
        self.totalElves = 10
        self.money = 100
        self.sentOut = 0
        self.atHome = 0
        self.safeReturn = 0
        self.safeHome = 0
        self.rolls = []
        self.elvesTotal = 0
        self.elvesLost = 0

    def beforeRoll(self):
        sentOut = 0
        print("Total Elves:" + str(color.GREEN), self.totalElves, color.WHITE)
        print("Total Money:" + str(color.GREEN) + " $" + str(self.money), color.WHITE)
        while self.carryOn:
            try:
                sentOut = int(input('Elves sent out: '))
                if sentOut > self.totalElves:
                    print('You do not have that many elves')
                else:
                    self.carryOn = False
            except ValueError:
                print(color.BRIGHT_RED + "ValueError - Invalid Input", color.WHITE)
        atHome = self.totalElves - sentOut
        print(color.GREEN + str(sentOut), color.WHITE + "elves sent out and" + color.GREEN, atHome, color.WHITE + "elves at home")
        self.atHome = atHome
        self.sentOut = sentOut

        self.carryOn = True
        return sentOut

    def rollDice(self, sent):
        moneyNone = "pardon"
        self.sentOut = sent
        money = self.money
        self.roll = random.randint(1, 6)
        self.rolls.append(self.roll)
        print("The dice roll was:" + str(color.GREEN), self.roll, color.WHITE)
        if self.roll == 1 or self.roll == 2:
            self.elvesLost += self.sentOut
            self.sentOut = self.sentOut - self.sentOut
            print(color.RED + messageOne + color.WHITE)

        elif self.roll == 3:
            self.elvesLost += self.atHome
            self.atHome = 0
            print(color.RED + str(messageTwo), color.WHITE)
            money = (self.sentOut * 10) + money

        elif self.roll == 4 or self.roll == 5:
            print(color.BRIGHT_GREEN + messageThree + color.WHITE)
            money = (self.sentOut * 10) + money

        elif self.roll == 6:
            print(color.BRIGHT_GREEN + messageFour + color.WHITE)
            money = (self.sentOut * 20) + money

        self.totalElves = self.sentOut + self.atHome

        print('Total money is', color.GREEN + '$' + str(money) + color.WHITE)
        print('Total elves:' + str(color.GREEN), self.totalElves, color.WHITE)
        self.money = money
        if self.totalElves == 0 and self.money == 0:
            moneyNone = "ah"

        return moneyNone

    def shop(self):
        buyElves = 0
        carryOn = self.carryOn
        if self.money > 0:
            while carryOn:
                try:
                    buyElves = int(input('How many elves would you like to buy (Elves cost $10 each)? '))
                    if int(buyElves) * 10 > self.money:
                        print(color.RED + 'You do not have enough money' + color.WHITE)
                    else:
                        carryOn = False
                        self.elvesTotal += int(buyElves)
                except ValueError:
                    print(color.BRIGHT_RED + 'Invalid Input' + color.WHITE)

            moneySpent = int(buyElves) * 10
            self.money = self.money - moneySpent

            self.totalElves = self.totalElves + buyElves
        print(self.totalElves)
        print(self.money)
        self.carryOn = True

    def eShop(self):
        elves = str(self.totalElves)
        if self.totalElves != 0:
            while self.carryOn:
                question = input(
                    "Would you like to sell the your remaining, " + elves + ", elves on elf-bay? [Y/N] ").lower()
                try:
                    if question == "y":
                        self.money = self.money + (self.totalElves * 5)
                        print("You have sold" + color.GREEN, self.totalElves, color.WHITE + "elves for", self.totalElves * 5)
                        self.totalElves = 0
                    elif question == "n":
                        print('You still have' + color.GREEN, self.totalElves,  str(color.WHITE))
                    self.carryOn = False
                except SyntaxError:
                    print(color.BRIGHT_RED + "I really don't now what has gone on..." + color.WHITE)

        self.carryOn = True

    def scores(self):
        print('\n--- Elf Game Stats ---')
        print('Your total money made was:', self.money)
        print('Your total elves was:', self.totalElves)
        print('Your rolls were:', self.rolls)
        print('Total elves gained:', self.elvesTotal)
        print('Total elves lost:', self.elvesLost)

    def data(self, ver, name):
        with open('elfGameData.txt', 'a') as file:
            data = ver + ", " + name + ", " + str(self.rolls) + ", " + str(self.money) + ", " + str(self.totalElves) + "\n"
            file.write(data)


elf = Elf()

username = input("Enter your name: ")

for x in range(10):
    print('\nRound', x + 1,  "out of 10")
    out = elf.beforeRoll()
    noMoney = elf.rollDice(out)
    if noMoney == "ah":
        print('You have gone broke!')
        break
    if x != 9:
        elf.shop()

elf.eShop()
elf.scores()
elf.data(version, username)
