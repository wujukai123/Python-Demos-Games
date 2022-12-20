def check_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt<3:
        if guess.lower()==answer.lower():
            print('Correct answer')
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input('Sorry wrong answer. Try again.')
            attempt=attempt+1
    if attempt==3:
        print('The correct answer is '+answer)
        score=0
print('Guess the Animal!')
guess1=input('Which bear lives at the North Pole?')
check_guess(guess1,'polar bear')
guess2=input('Which is the fastest land animal?')
check_guess(guess2,'cheetah')
guess3=input('Which is the largest animal?')
check_guess(guess3,'blue whale')
guess4=input('How many hearts does an octopus have?')
check_guess(guess4,'three')
guess5=input('Which is the loudest animal?')
check_guess(guess5,'blue whale')
guess6=input('Which is the slowest animal?')
check_guess(guess6,'bradypod')
guess7=input('Which is the tallest animal?')
check_guess(guess7,'girraffe')
guess8=input('Which animal has a long nose?')
check_guess(guess8,'elephant')
guess9=input('Which animal has a long ear?')
check_guess(guess9,'rabbit')
guess10=input('Which is the longest tail animal in the world?')
check_guess(guess10,'long tail cock')
print('Your score is '+str(score))
