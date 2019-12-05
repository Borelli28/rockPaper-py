import random

class Tictactoe:
    
    def __init__(self):
        self.options = ["Rock", "Paper", "Scissors"]
        self.user_pick = ""
        self.cpu_pick = ""
        self.cpu_counter = 0
        self.user_counter = 0

    #This method contains and run the whole game
    def program(self):

        #while loop to play again if user choose [Y]. If [N] program ends.
        while True:

            #Ask user for his choice(Rock, Paper or Scissors). Then print his choice as a str and store the value in user_pick for further use.
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

            else:
                self.user_pick = "Invalid"
                print("ERROR: Invalid Input")


            # CPU choose a random pick from options list(rock, paper, scissors), print the cpu pick and store the value in cpu_pick for further use.
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
            #If user pick is invalid then just print the statement
            if self.user_pick == "Invalid":
                print("User Fucked the Game Up!\n")

            #If both players choose same pick announce it as a draw
            elif self.cpu_pick == self.user_pick:
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


            #user choose rock and wins
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

                
            #Show current count of both players and also ask(while loop) the user if he want to continue playing.
            print("You: {usercounter} | CPU: {cpucounter}".format(usercounter=self.user_counter, cpucounter=self.cpu_counter))
            print(" ")
            print("**********************\n")

            #if [Y] restart game(play another game), if [N] entire program ends.
            while True:
                rawAnswer = input("Want to Play Again[Y] or [N]: ")
                answer = rawAnswer.capitalize()
                if answer in ("Y", "N"):
                    break
                print("invalid Input")
            if answer == "Y":
                continue
            else:
                print("Thanks for Playing...\n")
                break


#run the game
classInstance = Tictactoe()
game = classInstance.program()
print(game)
