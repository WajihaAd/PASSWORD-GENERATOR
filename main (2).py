import random
import time
from tqdm import tqdm
import os

class password1:
    def __init__(self,length):
        self.length = length
        self.result = ""

    def Generator(self):
        choice2 = []
        from passwordg import all_characters as ch
        if __name__ == "__main__":
            for i in tqdm(range(self.length), desc="Generating Password", unit="chars", leave=False):
                choice1 = random.choice(ch)
                choice2.append(choice1) 
                time.sleep(1) 
            self.result = ''.join(choice2) 

    def resultfinal(self):
        print ("Processing..... Almost there")
        time.sleep(2)
        print("Processing complete.")
        os.system('clear')
        print(f"Password is: {self.result}")  


def main(): 
    os.system('clear')
    a="\033[1mWelcome to the password generator\033[0m"
    print(a.center(60))
    while True:
        g = input("Enter the length of the password: ")
        try:
            g = int(g)
            if g <= 0:
                raise ValueError("Invalid input. Please enter a positive integer.")
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    l = password1(g)
    l.Generator()
    l.resultfinal()

main()
