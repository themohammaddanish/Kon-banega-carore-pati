# Initializing the quiz
total_prize = 0

questions = [
    "What is the capital of Nepal?" , 
    "Which is the highest mountain in Nepal?",
    "Which of the following is the national flower of Nepal?",
    "Who is considered the founder of modern Nepal?",
    "What is the official language of Nepal?",
    "Which river is known as the longest river in Nepal?",
    "What is Nepal’s national animal?",
    "Lumbini, the birthplace of Lord Buddha, is located in which province?",
    "When does Nepal celebrate its Constitution Day?",
    "What is the currency of Nepal?"
]

options = [
    ["A) Pokhara", "B) Kathmandu", "C) Bhaktapur", "D) Lalitpur"],  
    ["A) Kangchenjunga", "B) Makalu", "C) Mount Everest", "D) Dhaulagiri"],  
    ["A) Lotus", "B) Rhododendron", "C) Sunflower", "D) Orchid"],  
    ["A) Prithvi Narayan Shah", "B) Tribhuvan Bir Bikram Shah", "C) King Mahendra", "D) Rana Bahadur Shah"],  
    ["A) Hindi", "B) English", "C) Nepali", "D) Newari"],  
    ["A) Bagmati", "B) Koshi", "C) Gandaki", "D) Karnali"],  
    ["A) Elephant", "B) Cow", "C) Tiger", "D) Snow Leopard"],  
    ["A) Province 1", "B) Gandaki Province", "C) Lumbini Province", "D) Bagmati Province"],  
    ["A) Baisakh 1", "B) Jestha 15", "C) Ashoj 3", "D) Kartik 20"],  
    ["A) Nepalese Dollar", "B) Nepalese Rupee", "C) Indian Rupee", "D) Yuan"]  
]

# Correct answers corresponding to each question (in lowercase)
correct_answers = ['b', 'c', 'b', 'a', 'c', 'd', 'b', 'c', 'c', 'b']

# Loop through all questions
for i in range(len(questions)):
    print(questions[i])
    for opt in options[i]:
        print(opt)

    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == correct_answers[i]:
        print("You are right and you won 1000")
        total_prize += 1000
    else:
        correct_option_index = ord(correct_answers[i]) - ord('a')
        print("Your are wrong the correct answer is:", options[i][correct_option_index])

print("\nWell played! You won a total of", total_prize)


ask enter 
hello world
afgoellh123 afgdorlw123
