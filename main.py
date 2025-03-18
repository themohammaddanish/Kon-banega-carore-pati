'''Inisializing the Question '''
total_prize=0
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

#for first qustion 
print(question[0])
print(options[0])
      
answer=str(input())
if (answer == "b"):
  print(" Your are right and you won 1000")
  total_prize +=100

else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[0][1] )

#for second qustion 
print(question[1])

print(options[1])
      
answer=str(input())
if (answer == "c"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[1][2] )
  
#for third qustion 
print(question[2])

print(options[2])
      
answer=str(input())
if (answer == "b"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[2][2] )
  
#for fourth qustion 
print(question[3])

print(options[3])
      
answer=str(input())
if (answer == "a"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[3][0] )
  
#for fifth qustion 
print(question[4])


print(options[4])
      
answer=str(input())
if (answer == "c"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[4][2] )
  
#for sixth qustion 
print(question[5])

print(options[5])
      
answer=str(input())
if (answer == "d"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[5][3] )
  
#for seventh qustion 
print(question[6])

print(options[6])
      
answer=str(input())
if (answer == "b"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[6][1] )
  
#for eight qustion 
print(question[7])

print(options[7])
      
answer=str(input())
if (answer == "c"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[7][2] )
  
#for ninth qustion 
print(question[8])

print(options[8])
      
answer=str(input())
if (answer == "c"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[8][2] )
  
#for tenth qustion 
print(question[9])

print(options[9])
      
answer=str(input())
if (answer == "b"):
  print(" Your are right and you won 1000")
  total_prize +=1000
else:
  print("tmse na hopayega bhaya sahi answer ye hai", options[9][1] )

print("well played you won", total_prize )