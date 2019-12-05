import csv

questions = []
answers1 = []
answers2 = []
answers3 = []
correct_answers = []

qnum = 1

score = []
 
with open("quiz.csv", newline='') as pythontext:
  reader = csv.reader(pythontext, delimiter = ';')
  for row in reader:
    questions.append(row[0])
    answers1.append(row[1])
    answers2.append(row[2])
    answers3.append(row[3])
    correct_answers.append(row[4])

while qnum < len(questions):
  print(questions[qnum])
  print(answers1[qnum])
  print(answers2[qnum])
  print(answers3[qnum])
  option = input("Выберите вариант ответа: ")

  if option == 'a':
    if answers1[qnum] == correct_answers[qnum]:
      print("_______________________________________________________Правильно_____")
      score.append(5)
    else:
      print("_______________________________________________________Неправильно_____")
  elif option == 'b':
    if answers2[qnum] == correct_answers[qnum]:
      print("_______________________________________________________Правильно_____")
      score.append(5)
    else:
      print("_______________________________________________________Неправильно_____")
  elif option == 'c':
    if answers3[qnum] == correct_answers[qnum]:
      print("_______________________________________________________Правильно_____")
      score.append(5)
    else:
      print("_______________________________________________________Неправильно_____")
  else:
    print("!!!!!_________________________Такого варинта ответа не существует_____!!!!!")

  qnum += 1

totalscore = sum(score)
print("Вы набрали " + str(totalscore) + " баллов")

if totalscore == 100:
  print("Ваша оценка 'A'")
elif totalscore == 95:
  print("Ваша оценка '+B'")
elif totalscore == 90:
  print("Ваша оценка 'B'")
elif totalscore == 85:
  print("Ваша оценка '-B'")
elif totalscore == 80:
  print("Ваша оценка '+C'")
elif totalscore == 75:
  print("Ваша оценка 'C'")
elif totalscore == 70:
  print("Ваша оценка '-C'")
elif totalscore == 65:
  print("Ваша оценка 'D'")
elif totalscore == 60:
  print("Ваша оценка '-D'")
else:
  print("Ваша оценка 'F'")


    

