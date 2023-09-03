import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
print("Hello and welcome to Sai Jagadesh's Quiz Game! ")
print("This quiz is based on GK & Space Science")
print("This trivia contains 10 Question consisting of 1 mark each ! All the Best")
print("NOTE: A small spelling mistake makes you lose points !")
import time
score = 0
total_q = 1
time.sleep(2.0)
#Question 1
ans = input("1. Amundsen, who was the first person to discover the South Pole, was the native of (norway/india/canada/sweden): ")
if ans.lower() == 'norway':
    score += 1
    print("Correct")
else:
    print("Incorrect. Amundsen was the native of Norway ! :)")
print("--------------------------------------------------------------------")
#Question 2    
time.sleep(2.0)
ans = input("2. Pandit Shivkumar Sharma is related to(shennai/violin/veena/santoor): ")
if ans.lower() == 'santoor':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is Santoor")
print("--------------------------------------------------------------------")
#Question 3    
time.sleep(2.0)
ans = input("3. The trophy ‘Davis Cup’ is related to (baseball/football/tennis/rugby): ")
if ans.lower() == 'tennis':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is tennis.")
print("--------------------------------------------------------------------")
#Question 4
time.sleep(2.0)
ans = input("4. The book, ‘Wealth of Nations,’ was written by (adam/david/karl/milton): ")
if ans.lower() == 'adam':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is Adam")
print("--------------------------------------------------------------------")
#Question 5
time.sleep(2.0)
ans = input("5. Who was the first Indian who won Palk-Strait Ocean Swimming Contest? (Alok/Baidyanath/Prabhat/Satish): ")
if ans.lower() == 'baidyanath':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is Baidyanath !")    
time.sleep(1.0)
print("--------------------------------------------------------------------")
print("You have sucessfully completed the GK QUIZ !! But wait Space quiz is there for you wait for 5 seconds.")
time.sleep(5.0)
#Question 6    
ans = input("6. Where are ISRO satellites made?(Short form of satellite center is enough):  ")
if ans.lower() == 'isac':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is ISAC or isac")
print("--------------------------------------------------------------------")
#Question 7    
time.sleep(2.0)
ans = input("7. What is the first Indian satellite ? (Bhaskara I/INSAT-1A/Aryabhata/Cartosat-1): ")
if ans.lower() == 'aryabhata':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is Aryabhata")
print("--------------------------------------------------------------------")
#Question 8    
time.sleep(2.0)
ans = input("8. In which year Aryabhata satellite was launched? (1976/1974/1975/1966): ")
if ans == '1975':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is 1975")
print("--------------------------------------------------------------------")
#Question 9
time.sleep(2.0)
ans = input("9.In which year Chandrayaan 1 was launched ? (2007/2008/2006/2009): ")
if ans == '2008':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is 2008")
print("--------------------------------------------------------------------")
#Question 10
time.sleep(2.0)
ans = input("10.What is the approx. budget for Chandrayaan 1 in (crores)(380/386/375/300):Rs.")
if ans == '386':
    score += 1
    print("Correct")
else:
    print("Incorrect. The correct answer is 386 crores")
print("--------------------------------------------------------------------")
time.sleep(2.0)
print("Do you know ?? \n Hardwork never fails - Just a quote")
time.sleep(2.0)
print("Here comes your score !!")
time.sleep(2.0)
print("Thanks for taking Smarticus Trivia ! You got ",score," questions correct")
if score>8:
    print("Well done !! and Bye !!You have good thirst")
    time.sleep(2.0)
    print("Best wishes,Sai Jagadesh")
else:
  print("Thanks and Bye !! ")
  time.sleep(2.0)
  print("Best wishes, Sai Jagadesh")
print("--------------------------------------------------------------------")
time.sleep(2.0)

