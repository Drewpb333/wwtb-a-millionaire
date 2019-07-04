# dictionary containing multiple dictionaries.  One dictionary for each question
questions = {}
questions['question1'] = {
    'question': 'Python is run on what type of machine?', 'correct_answer': 'C', 'points': 100}
questions['question2'] = {
    'question': 'Who is the creator of Python?', 'correct_answer': 'B', 'points': 200}
questions['question3'] = {
    'question': 'Why is Python a relatively easy language to learn?', 'correct_answer': 'D', 'points': 500}
questions['question4'] = {
    'question': 'Which of the following best describes Python?', 'correct_answer': 'B', 'points': 1000}
questions['question5'] = {
    'question': 'Python can be used in which of the following programming paradigms?', 'correct_answer': 'D', 'points': 2000}

# Answer Choices
questions['question1']['answer_choices'] = "\nA. Car engine\nB. Sewing machine\nC. Computer\nD. CD Player"
questions['question2']['answer_choices'] = "\nA. James Gosling\nB. Guido van Rossum\nC. Brendan Eich\nD. Bjarne Stroustrup"
questions['question3']['answer_choices'] = "\nA. Simple syntax\nB. Dynamically Typed\nC. Strong Online Community\nD. All of the Above"
questions['question4']['answer_choices'] = ("\nA. Markup language\nB. High-level, general-purpose programming language"
                                            "\nC. Assembly language\nD. Machine Language")
questions['question5']['answer_choices'] = "\nA. Functional\nB. Procedural\nC. Object-Oriented\nD. All of the Above"

# Remaining global variables
valid_answers = ['A', 'B', 'C', 'D']
total_points = 0


def main():
    start_game()

    # asks user each question from the dictionary
    for i in questions:
        question_prompt(i)

    check_highest_score()
    play_again()


def start_game():
    print('Welcome to Who Wants to Be a Millionaire!\n')
    global total_points
    total_points = 0

# prints question and asks for user's response
def question_prompt(question):
    current_question = questions[question]
    print(current_question['question'])
    print(current_question['answer_choices'])
    user_answer = input('\nEnter the letter of the correct answer: ')
    check_answer(user_answer, current_question)


def check_answer(answer, question):
    answer = answer.upper()
    if answer not in valid_answers:
        while answer not in valid_answers:
            answer = input(
                "Invalid Input.  Enter a choice of 'A', 'B', 'C', or 'D'\n")
    if answer == question['correct_answer']:
        global total_points
        total_points += question['points']
        print(f'Correct!  Your current point total is {total_points}.\n')
    else:
        print(f'Incorrect.  Your current point total is {total_points}.\n')


def check_highest_score():
    highScoreCard = open('highscore.txt', 'r')
    highScore = highScoreCard.readline().split()
    if len(highScore) > 0:
        # retrieves score in case user enters more than one name
        highScore = int(highScore[len(highScore) - 1])
    else:
        # if scorecard is blank
        highScore = 0
    highScoreCard.close()
    if(total_points > highScore):
        newScoreCard = open('highscore.txt', 'w')
        name = input(
            'Congratulations! You have the newest high score! Please enter your first name: ')
        newScoreCard.write(f'{name} {total_points}')
        newScoreCard.close()
    elif(total_points == highScore):
        newScoreCard = open('highscore.txt', 'a')
        name = input(
            'Congratulations! Your score is tied for first place! Please enter your first name: ')
        newScoreCard.write(f'\n{name} {total_points}')
        newScoreCard.close()


def play_again():
    new_game = input('Game over. Would you like to play again? Type "Y" or "N"\n')
    if(new_game.upper() == 'Y'):
        main()
    elif(new_game.upper() == 'N'):
        print('\nThanks for playing.')
    else:
        print('\nInvalid input.  Please type "Y" for yes or "N" for no\n')


main()