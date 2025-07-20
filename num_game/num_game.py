import random

# Initialize the game state
low = 1
high = 10

current_number = random.randint(low,high)
score =0

print("-----------------------------------------------------------------\n")
print("Welcome to the Number Guessing Game!")
print("Rules: Guess if the next number will be Greater (G) or Smaller (S).\n")

while True:
    print("-----------------------------------------------------------------")
    print(f"The current number is: {current_number}")
    print("Guess the next number")
    guess = input("Greater(G), Smaller(S) or to Quit(Q): ").upper()
    
    next_number = random.randint(low,high)
    
    if(guess=="Q"):
        print("-----------------------------------------------------------------")
        print(f"Your total winnings: ${score}")
        print("Thanks For Playing!")
        print("-----------------------------------------------------------------")
        break
    elif(guess=="G" and next_number>=current_number):
        print("-----------------------------------------------------------------")
        print("✅ Correct! The number went Up.")
        current_number=next_number
        score+=1
    elif(guess=="S" and next_number<=current_number):
        print("-----------------------------------------------------------------")
        print("✅ Correct! The number went Up.")
        current_number=next_number
        score+=1
    elif(guess == "S" and next_number>current_number):
        print("-----------------------------------------------------------------")
        print("❌ Wrong! The number went Down.")
        current_number=next_number
        score=0
    elif(guess == "G" and next_number<current_number):
        print("-----------------------------------------------------------------")
        print("❌ Wrong! The number went Down.")
        current_number=next_number
        score=0
    else:
        print("-----------------------------------------------------------------")
        print("⚠️ Invalid input. Please enter G, S, or Q.")
