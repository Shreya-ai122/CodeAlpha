import random
#List of predefined words
word_list = ["apple", "banana", "cherry", "date", "elder"]

#Select a random word from the list
selected_word = random.choice(word_list)

#Create variable to store the guessed letters
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

#Create the display word
display_word = ["_" for _ in selected_word]

print("Welcome to Hangman Game!")
print("Guess the word(but one letter at a time)!")
print("You have", max_attempts, "attempts to guess the word!")

#Start the game loop
while incorrect_guesses < max_attempts and "_" in display_word:
  print("       ")
  print("Word:", " ".join(display_word))
  guess = input("Enter a letter: ").lower()
  if guess in guessed_letters:
    print("You already guessed that letter. Try again.")
    continue
  guessed_letters.append(guess)
  if guess in selected_word:
    print("Good guess!")
    for i in range(len(selected_word)):
      if selected_word[i] == guess:
        display_word[i] = guess
  else:
    print("Incorrect guess.")
    incorrect_guesses += 1
    print("You have", max_attempts - incorrect_guesses, "attempts left.")
    
#Game result
if "_" not in display_word:
  print("Congratulations! You guessed the word:", selected_word)
  print("You win!")
else:
  print("Sorry, you ran out of attempts. The word was:", selected_word)


