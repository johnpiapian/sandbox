class Ques:
    def __init__(self, question, options, correct):
        self.qa_map = ["A", "B", "C", "D"]
        self.userAnswer = -1
        self.question = question
        self.options = options
        self.correct = correct

    def getQuestion(self):
        return self.question

    def getOptions(self):
        return self.options

    def checkAnswer(self, index):
        return self.correct == index

    def isValidOption(self, option):
        return option in self.qa_map

    def isAnswerCorrect(self):
        return self.correct == self.userAnswer

    def setUserAnswer(self, answer):
        self.userAnswer = self.qa_map.index(answer)

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{self.qa_map[i]}) {option}")

    def display_feedback(self):
        if self.isAnswerCorrect():
            print("Dang you are smart!!")
        else:
            print("Bro.. I am very disappointed!!")


def displayScore(questions):
    correct_count = 0
    for i, item in enumerate(questions, start=1):
        if item.isAnswerCorrect():
            correct_count += 1
        print(f"{i} : {item.isAnswerCorrect()}")
    score = (correct_count / len(questions)) * 100
    print(f"\n\nYour score is {round(score)}%!\n")


def app():
    questions = list()
    questions.append(Ques("What is your name?", ["John", "James", "Joe", "Smith"], 0))
    questions.append(Ques("What is your friends name?", ["John", "James", "Joe", "Smith"], 2))
    questions.append(Ques("What is your age?", [23, 24, 25, 26], 0))

    for item in questions:
        item.display()
        # user would type a letter answer
        user_answer = input("Select an option: ").upper()
        while not item.isValidOption(user_answer):
            user_answer = input("Invalid input (Reenter): ").upper()

        item.setUserAnswer(user_answer)
        item.display_feedback()
        print()

    displayScore(questions)

app()
