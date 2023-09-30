import random

#  30 questions with answer choices
questions = [
    {"question": "What is the capital of France?",
     "options": ["a) London", "b) Paris", "c) Berlin", "d) Madrid"],
     "answer": "b) Paris"},
    {"question": "Which planet is known as the Red Planet?",
     "options": ["a) Mars", "b) Venus", "c) Jupiter", "d) Saturn"],
     "answer": "a) Mars"},
    {"question": "What is the largest mammal in the world?",
     "options": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Polar Bear"],
     "answer": "b) Blue Whale"},
      {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "b) Carbon Dioxide"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Go", "b) Gl", "c) Au", "d) Ag"],
        "answer": "c) Au"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["a) Charles Dickens", "b) Mark Twain", "c) William Shakespeare", "d) Jane Austen"],
        "answer": "c) William Shakespeare"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["a) 5", "b) 6", "c) 7", "d) 8"],
        "answer": "c) 7"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["a) Heart", "b) Liver", "c) Skin", "d) Brain"],
        "answer": "c) Skin"
    },
    {
        "question": "What is the symbol for the element oxygen?",
        "options": ["a) O2", "b) Ox", "c) Om", "d) O"],
        "answer": "d) O"
    },
    {
        "question": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "c) Nitrogen"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "c) Jupiter"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["a) Pablo Picasso", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Michelangelo"],
        "answer": "c) Leonardo da Vinci"
    },
    {
        "question": "Which gas do humans breathe out when they exhale?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "b) Carbon Dioxide"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) H2O", "b) Wt", "c) Wa", "d) H2"],
        "answer": "a) H2O"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["a) 0", "b) 1", "c) 2", "d) 3"],
        "answer": "c) 2"
    },
    {
        "question": "Who was the first person to walk on the Moon?",
        "options": ["a) Neil Armstrong", "b) Buzz Aldrin", "c) Yuri Gagarin", "d) John Glenn"],
        "answer": "a) Neil Armstrong"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["a) China", "b) South Korea", "c) Japan", "d) Thailand"],
        "answer": "c) Japan"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["a) Amazon", "b) Mississippi", "c) Nile", "d) Yangtze"],
        "answer": "c) Nile"
    },
    {
        "question": "What is the chemical symbol for silver?",
        "options": ["a) Si", "b) Ag", "c) Sl", "d) Sr"],
        "answer": "b) Ag"
    },
    {
        "question": "Which gas do plants give off during photosynthesis?",
        "options": ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "answer": "a) Oxygen"
    },
    {
        "question": "What is the largest species of shark?",
        "options": ["a) Great White Shark", "b) Hammerhead Shark", "c) Whale Shark", "d) Tiger Shark"],
        "answer": "c) Whale Shark"
    },
    {
        "question": "Who is known as the 'Father of Modern Physics'?",
        "options": ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Stephen Hawking"],
        "answer": "b) Albert Einstein"
    },
    {
        "question": "What is the chemical symbol for helium?",
        "options": ["a) H", "b) He", "c) Hee", "d) Hel"],
        "answer": "b) He"
    },
    {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["a) Mercury", "b) Venus", "c) Mars", "d) Jupiter"],
        "answer": "b) Venus"
    },
    {
        "question": "How many bones are there in the adult human body?",
        "options": ["a) 150", "b) 180", "c) 206", "d) 250"],
        "answer": "c) 206"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["a) J.K. Rowling", "b) Harper Lee", "c) F. Scott Fitzgerald", "d) George Orwell"],
        "answer": "b) Harper Lee"
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["a) Sahara", "b) Gobi", "c) Arabian", "d) Kalahari"],
        "answer": "a) Sahara"}

]

def ask_question():

    random_question = random.choice(questions)


    print(random_question["question"])
    for option in random_question["options"]:
        print(option)

    user_answer = input("Your answer (enter the letter of your choice): ")

    if user_answer.lower() == random_question["answer"].lower()[0]:  # Extract the letter from the answer
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {random_question['answer']}.\n")


while True:
    ask_question()

    if len(questions) == 0:
        print("Congratulations! You've completed the quiz.")
        break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
    print("thank you")