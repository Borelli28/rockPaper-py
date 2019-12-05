import random


class Tictactoe:

    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_pick = ""
        self.cpu_pick = ""
        self.cpu_counter = 0
        self.user_counter = 0
        self.game_counter = 1

    #This method contains and run the whole game
    def program(self):

        #while nobody has won 3 games execute entire program() code
        while self.user_counter < 3 and self.cpu_counter < 3:

            #Ask user for his choice(Rock, Paper or Scissors). Then print his choice as a str and store the value in user_pick for further use.
            print("Game: {count}\n".format(count=self.game_counter))
            print("Make a Pick: \n")
            raw_userChoice = input("[A] for Rock, [S] for Paper & [D] for Scissors:  ")
            user_input = raw_userChoice.capitalize()
            print(" ")

            if user_input == "A":
                self.user_pick = "Rock"
                print("You choose: {pick}!".format(pick=self.user_pick))

            elif user_input == "S":
                self.user_pick = "Paper"
                print("You choose: {pick}!".format(pick=self.user_pick))

            elif user_input == "D":
                self.user_pick = "Scissors"
                print("You choose: {pick}!".format(pick=self.user_pick))

            elif user_input != "A" or "S" "D":
                return "Use [A], [S] or [D] keys. Try Again!"
            #***********  put a restar game here ***********


            #CPU choose a random pick from options list(rock, paper, scissors), print the cpy pick and store the value in cpu_pick for further use.
            print(" ")
            raw_cpu_pick = random.choice(self.options)

            if raw_cpu_pick == "Rock":
                self.cpu_pick = "Rock"
                print("CPU choose: {pick}!".format(pick=self.cpu_pick))

            elif raw_cpu_pick == "Paper":
                self.cpu_pick = "Paper"
                print("CPU choose: {pick}!".format(pick=self.cpu_pick))

            elif raw_cpu_pick == "Scissors":
                self.cpu_pick = "Scissors"
                print("CPU choose: {pick}!".format(pick=self.cpu_pick))


            #Compare both picks and announce the winner. Plus add 1 to the counter of the winner.
            print(" ")
            #If both players choose same pick announce it as a draw
            if self.cpu_pick == self.user_pick:
                print("Its a Draw!\n")

            #cpu choose rock and wins
            elif self.cpu_pick == "Rock" and self.user_pick == "Scissors":
                print("CPU Wins\n")
                self.cpu_counter += 1

            #cpu choose paper and wins
            elif self.cpu_pick == "Paper" and self.user_pick == "Rock":
                print("CPU Wins\n")
                self.cpu_counter += 1

            #cpu choose scissors and wins
            elif self.cpu_pick == "Scissors" and self.user_pick == "Paper":
                print("CPU Wins\n")
                self.cpu_counter += 1


            # user choose rock and wins
            elif self.user_pick == "Rock" and self.cpu_pick == "Scissors":
                print("You Won!\n")
                self.user_counter += 1

            #user choose paper and wins
            elif self.user_pick == "Paper" and self.cpu_pick == "Rock":
                print("You Won!\n")
                self.user_counter += 1

            #user choose scissors and wins
            elif self.user_pick == "Scissors" and self.cpu_pick == "Paper":
                print("You Won!\n")
                self.user_counter += 1

            #Show current count of both players. Also it at the end it will add 1 to the total games played counter
            print("You: {usercounter} | CPU: {cpucounter}".format(usercounter=self.user_counter, cpucounter=self.cpu_counter))
            print(" ")
            print("**********************\n")
            self.game_counter += 1

        #If the someone counter hits 3, it will anounce the winner of the game
        if self.cpu_counter == 3:
            print("CPU Won The Game...\n")

        else:
            print("YOU WON THE GAME!\n")
            

# run the game
classInstance = Tictactoe()
game = classInstance.program()
print(game)
