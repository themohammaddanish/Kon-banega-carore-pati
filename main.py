'''Inisializing the Question '''
question=["What is the capital of Nepal?" , 
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
    ["Pokhara", "Kathmandu", "Bhaktapur", "Lalitpur"],  
    ["Kangchenjunga", "Makalu", "Mount Everest", "Dhaulagiri"],  
    ["Lotus", "Rhododendron", "Sunflower", "Orchid"],  
    ["Prithvi Narayan Shah", "Tribhuvan Bir Bikram Shah", "King Mahendra", "Rana Bahadur Shah"],  
    ["Hindi", "English", "Nepali", "Newari"],  
    ["Bagmati", "Koshi", "Gandaki", "Karnali"],  
    ["Elephant", "Cow", "Tiger", "Snow Leopard"],  
    ["Province 1", "Gandaki Province", "Lumbini Province", "Bagmati Province"],  
    ["Baisakh 1", "Jestha 15", "Ashoj 3", "Kartik 20"],  
    ["Nepalese Dollar", "Nepalese Rupee", "Indian Rupee", "Yuan"]  
]

print(question[0])

for i in range(1):
      print(options[0])
      
answer=str(input())
if (answer == options[0][1]):
  print("you won 1000")
else:
  print("the anser is", options[0][1] )
  
