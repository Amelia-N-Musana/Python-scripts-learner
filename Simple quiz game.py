questions = ("How many colours are on the German flag?",
             "What percentage of water is the body made up of?",
             "What is the interior angle sum of a triangle?",
             "Which of the following is an object oriented programming language?",
             "What is the term used to describe a person who is afraid of spiders?")

options = (("A. 7", "B. 5", "C. 3", "D. 1"),
           ("A. 75%", "B. 40%", "C. 10%", "D. 60%"),
           ("A. 360°", "B. 90°", "C. 180°", "D. 540°"),
           ("A. C", "B. JAVA", "C. Fortran", "D. Haskell"),
           ("A. Arachnophobia", "B. Claustrophobia", "C. Entomophobia", "D. Acrophobia"))

answers = ("C", "D", "C", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-----------------------")
print("RESULTS")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"You're score is: {score}%")
