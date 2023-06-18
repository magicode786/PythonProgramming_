from random import randint
class GuessGame:
    def __init__(self):
        pass
    def GuesstheNumber(self):
        pass
class guessGame(GuessGame):
    def __init__(self, input_number, chance):
        self.input_number = input_number
        self.chance = chance
    def GuesstheNumber(self):
        random_number_to_guess = randint(1,20)
        if self.input_number == random_number_to_guess:
            print(f"The number you guessed is {self.input_number}")
            print(f"The random  number  is {random_number_to_guess}")
            print("Congratulations!!!! You have won the Guessing Game")
            return random_number_to_guess
            #it should break once guess is correct
        else:
            print(f"The number you guessed is {self.input_number}")
            print(f"The random  number  is {random_number_to_guess}")
            self.chance = self.chance - 1
            if self.chance >= 1:
                print(f"Try Again! You have {self.chance} more chances, Good Luck")
                return random_number_to_guess
            else:
                print(f"Better luck next time, Thanks for Participating")
                return random_number_to_guess
def main():
    chance = 3
    while(chance<=3):
        guessed_number =  gettheGuessednumber()
        won_or_loose = guessGame(guessed_number, chance)
        randomNumber = won_or_loose.GuesstheNumber()
        #print(f"won or loosse {randomNumber}")
        if randomNumber == guessed_number:
            break
        chance  = chance - 1
        if chance <=0:
            break
def gettheGuessednumber():
    number = int(input("Enter the no of your choice betwen 1 to 20\n"))
    print("are you ready to check your intelligence and luck")
    return number

if __name__ == "__main__":
    main()

