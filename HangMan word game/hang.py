import random

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition']
word = random.choice(words)
guess = ''
turns = 10
while turns > 0:
    for c in word:
        if c in guess:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()
    guesses = input("enter the guess")
    guess = guess + guesses
    if guess not in word:
        turns = turns - 1
