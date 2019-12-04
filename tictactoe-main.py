import random

class Tictactoe:

                #["Rock", "Paper", "Scissors"]
    def __init__(self):
        self.options = [0, 1, 2]
        self.user_pick = 0
        self.cpu_pick = 0
        self.bestOfThree = 0
        self.cpu_counter = 0
        self.user_counter = 0

#ask and saved user input(rock, paper or scissors) as the index in the options list
    def program(self):

        while self.bestOfThree >3:
            print("Make a Pick: \n")
            user_input = input("[1] for Rock, [2] for Paper & [3] for Scissors")


            if user_input == 1:
                print("You choose: Rock!\n")

            elif user_input == 2:
                print("You choose: Paper!\n")
                self.user_pick += 1

            elif user_input == 3:
                print("You choose: Scissors!\n")
                self.user_pick += 2

            else:
                print("ERROR: Invalid Input. Try Again!")

            print(".................")

#calculate a cpu pick and saved it in self.cpu_pick as a index number in self.option list

            print(".................")
            print("CPU making a pick...\n")
            self.cpu_pick = random.choice(self.options)
            print("CPU Made a Pick!\n")

#Grab Picks and calculate the winner

            if self.cpu_pick == self.user_pick:
                print("Tie\n")

        #cpu choose rock and wins
            elif self.cpu_pick == 0 and self.user_pick == 1 or 2:
                print("CPU: Rock\n")
                print("CPU Wins\n")
                self.bestOfThree += 1
                self.cpu_counter += 1

        #cpu choose paper and wins
            elif self.cpu_pick == 1 and self.user_pick == 0:
                print("CPU: Paper\n")
                print("CPU Wins\n")
                self.bestOfThree += 1
                self.cpu_counter += 1

        # cpu choose scissors and wins
            elif self.cpu_pick == 2 and self.user_pick == 1:
                print("CPU: Scissors\n")
                print("CPU Wins\n")
                self.bestOfThree += 1
                self.cpu_counter += 1

#

        # user choose rock and wins
            elif self.user_pick == 0 and self.cpu_pick == 1 or 2:
                print("CPU: Rock\n")
                print("You Won\n")
                self.bestOfThree += 1
                self.user_counter += 1

        # user choose paper and wins
            elif (self.user_pick == 1 and self.cpu_pick == 0):
                print("CPU: Paper\n")
                print("You Won\n")
                self.bestOfThree += 1
                self.user_counter += 1

        # user choose scissors and wins
            elif self.user_pick == 2 and self.cpu_pick == 1:
                print("CPU: Scissors\n")
                print("You Won\n")
                self.bestOfThree += 1
                self.user_counter += 1

#

        if self.bestOfThree == 3:
            if self.user_counter > self.cpu_counter:
                print("You Won The Game!\n")

            else:
                print("CPU Won The Game, Try Again!\n")

        else:
            print("Error: Error in software...\n")



#run the game
classInstance = Tictactoe()
game = classInstance.program()
print(game)




# 0         1       2             W       L
#Rock B. Paper, Scissors        0 > 1 and 2
#Paper B. Rock                  1 > 0 but < 2
#Scissors B. Paper              2 > 1 but < 0
