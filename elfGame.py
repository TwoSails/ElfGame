import random

version = "1.0.0"

print("------ Elf Game ------")


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
        print("Total Elves:", self.totalElves)
        while self.carryOn:
            try:
                sentOut = int(input('Elves sent out: '))
                if sentOut > self.totalElves:
                    print('You do not have that many elves')
                else:
                    self.carryOn = False
            except ValueError:
                print("ValueError - Invalid Input")
        atHome = self.totalElves - sentOut
        print(sentOut, "elves sent out and", atHome, "elves at home")
        self.atHome = atHome
        self.sentOut = sentOut

        self.carryOn = True
        return sentOut

    def rollDice(self, sent):
        self.sentOut = sent
        money = self.money
        self.roll = random.randint(1, 6)
        self.rolls.append(self.roll)
        print("The dice roll was:", self.roll)
        if self.roll == 1 or self.roll == 2:
            self.elvesLost += self.sentOut
            self.sentOut = self.sentOut - self.sentOut
            print('All the elves sent out died in a horrific gang related incident with goblins. the elves at home '
                  'are safe and unharmed, no money is made')

        elif self.roll == 3:
            self.elvesLost += self.atHome
            self.atHome = 0
            print('The elves at home all suffer from food poisoning and vomit to death, however the elves that were '
                  'sent out all return home safely with £10')
            money = (self.sentOut * 10) + money

        elif self.roll == 4 or self.roll == 5:
            print('The elves at home are all safe and the elves at work come back with £10 each')
            money = (self.sentOut * 10) + money

        elif self.roll == 6:
            print('The elves at home are all safe and the elves at work come back with £20 each')
            money = (self.sentOut * 20) + money

        self.totalElves = self.sentOut + self.atHome

        print('Total money is $' + str(money))
        print('Total elves:', self.totalElves)
        self.money = money

    def shop(self):
        carryOn = self.carryOn
        while carryOn:
            try:
                buyElves: int = int(input('How many elves would you like to buy? '))
                if buyElves * 10 > self.money:
                    print('You do not have enough money')
                else:
                    carryOn = False
                    self.elvesTotal == buyElves
            except ValueError:
                print('Invalid Input')

        moneySpent = buyElves * 10
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
                    "Would you like to sell the your remaining, " + elves + ", elves on elf-bay? [Y/N]").lower()
                try:
                    if question == "y":
                        self.money = self.money + (self.totalElves * 5)
                        print("You have sold", self.totalElves, "elves for", self.totalElves * 5)
                        self.totalElves = 0
                    elif question == "n":
                        print('You still have', self.totalElves)
                    self.carryOn = False
                except SyntaxError:
                    print("I really don't now what has gone on...")

        self.carryOn = True

    def scores(self):
        print('\n--- Elf Game Stats ---')
        print('Your total money made was:', self.money)
        print('Your total elves was:', self.totalElves)
        print('Your rolls were:', self.rolls)
        print('Total elves gained:', self.elvesTotal)
        print('Total elves lost:', self.elvesLost)

    def data(self, ver):
        with open('elfGameData.txt', 'a') as file:
            data = ver + ", " + str(self.rolls) + ", " + str(self.money) + ", " + str(self.totalElves) + "\n"
            file.write(data)


elf = Elf()

for x in range(10):
    print('\nRound', x + 1,  "out of 10")
    out = elf.beforeRoll()
    elf.rollDice(out)
    elf.shop()

elf.eShop()
elf.scores()
elf.data(version)
