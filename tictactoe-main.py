import random

class Tictactoe:

    # ["Rock", "Paper", "Scissors"]
    def __init__(self):
        self.options = [0, 1, 2]
        self.user_pick = 0
        self.cpu_pick = 0
        self.cpu_counter = 0
        self.user_counter = 0

    # ask and saved user input(rock, paper or scissors) as the index in the options list
    def program(self):

        while self.user_counter < 3 or self.cpu_counter < 3:
            print("Make a Pick: \n")
            raw_userChoice = input("[A] for Rock, [S] for Paper & [D] for Scissors:  ")
            user_input = raw_userChoice.capitalize()

            if user_input == "A":
                print("You choose: Rock!")
                self.user_pick = 0

            elif user_input == "S":
                print("You choose: Paper!")
                self.user_pick = 1

            elif user_input == "D":
                print("You choose: Scissors!")
                self.user_pick = 2

            elif user_input != "A" or "S" "D":
                return "Use A, S or D keys. Try Again!"

            print(self.user_pick)


            # calculate a cpu pick and saved it in self.cpu_pick as a index number in self.option list
            print("CPU making a pick...\n")
            raw_cpu_pick = random.choice(self.options)

            if raw_cpu_pick == 0:
                print("CPU choose Rock!")
                self.cpu_pick = 0

            elif raw_cpu_pick == 1:
                print("CPU choose Paper!")
                self.cpu_pick = 1

            elif raw_cpu_pick == 2:
                print("CPU choose Scissors!")
                self.cpu_pick = 2

            print(self.cpu_pick)

            # Grab Picks and calculate the winner
            print(" ")
            if self.cpu_pick == self.user_pick:
                print("Tie\n")

            # cpu choose rock and wins
            elif self.cpu_pick == 0 and self.user_pick == 2:
                print("CPU: Rock\n")
                print("CPU Wins\n")
                self.cpu_counter += 1

            # cpu choose paper and wins
            elif self.cpu_pick == 1 and self.user_pick == 0:
                print("CPU: Paper\n")
                print("CPU Wins\n")
                self.cpu_counter += 1

            # cpu choose scissors and wins
            elif self.cpu_pick == 2 and self.user_pick == 1:
                print("CPU: Scissors\n")
                print("CPU Wins\n")
                self.cpu_counter += 1

            #

            # user choose rock and wins
            elif self.user_pick == 0 and self.cpu_pick == 2:
                print("CPU: Scissors\n")
                print("You Won\n")
                self.user_counter += 1

            # user choose paper and wins
            elif self.user_pick == 1 and self.cpu_pick == 0:
                print("CPU: Rock\n")
                print("You Won\n")
                self.user_counter += 1

            # user choose scissors and wins
            elif self.user_pick == 2 and self.cpu_pick == 1:
                print("CPU: Paper\n")
                print("You Won\n")
                self.user_counter += 1

            print("You: {usercounter} | CPU: {cpucounter}".format(usercounter=self.user_counter, cpucounter=self.cpu_counter))
        #

        if self.user_counter or self.cpu_counter == 3:
            if self.user_counter > self.cpu_counter:
                print("You Won The Game!\n")

            else:
                print("CPU Won The Game, Try Again!\n")




# run the game
classInstance = Tictactoe()
game = classInstance.program()
print(game)




# 0         1       2             W       L
#Rock B. Scissors               0 > 2 but < 1
#Paper B. Rock                  1 > 0 but < 2
#Scissors B. Paper              2 > 1 but < 0
