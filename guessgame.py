correct_word = "Tiger"
i = ""
guess_count = 1
guess_limit = 4
out_of_guesses = False

while i != correct_word and not (out_of_guesses):
    if guess_count < guess_limit:
        i = input(f"Enter {guess_count} guessing ")
        guess_count+= 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print ("out of guesses......YOU LOSE")
else:
    print ("YOU WON")