secret_number= 9
guess_count=0
guess_limit=3
print("\n\nYou have three guesses to figure out a secret number thats between 1-10\nBest of Luck!!\nGame On!")
while guess_count < guess_limit:
    guess=int(input('Guess:'))
    guess_count += 1
    if guess == secret_number:
        print('You Won!\nThe secret number is 9')
        break
else:
    print('Sorry you failed')    
