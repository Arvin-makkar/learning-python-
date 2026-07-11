print("Hello I am starting my python journey")\
name="Arvin"
print("My name is", name)
print('Hi')
print('👋Howdy')
print('Morning Dharma')
print('Evening Sonny')
print('       1')
print('     2 3')
print('   4 5 6')
print('7 8 9 10')
print('DDDD  L')
print('D  D  L')
print('D  D  L')
print('D  D  L')
print('D  D  L')
print('DDDD  L')
print('Congrats ! you\'ve made it to the end of chapter one!')
name = 'Erlich Bachman'
user_id = 16180339887
progress = 0.75
xp = 60 
verified = true
print(name)
print(user_id)
print(progress)
print(xp)
print(verified)
score = 0 
score = 4 + 3
score = 4 - 3
score = 4 * 3
score = 4 / 3
print(score)
pizza = 2.99
coke = 0.99
total = pizza + coke 
tip = total * 0.2 
print(tip)
temp_f = 76
temp_c = (temp_f - 32)/1.8
print(temp_c)
score = 5 % 3
print(score)
score = 5 % 2
print(score)
score = 5 % 1 
print(score)
score = 2 ** 2 
print(score)
score = 2 ** 3
print(score)
score = 2 ** 4 
print(score)
mass = 16 
height = 14
bmi = mass/height**2
print(bmi)
username = input('Arvin')
print(username)
age = int(input('18'))
print(age)
import math 
a = 12
b = 13 
c = 15
#calculate hypotenuse 
c = math.sqrt(a**2 + b**2)
print(c)
pesos = float(input("what do you have left in pesos? "))
soles = float(input("what do you have left in soles? "))
reais = float(input("what do you have left in reais? "))
usd = (pesos/56) + (soles/3.5) + (reais/5)
print(usd)
year = 2028
focus = 0.6
skin = 'My Mistake'
shedding = True 
print(year)
print(focus)
print(skin)
print(shedding)
balance = 480 
rate = 0.08
balance = balance +(balance * rate)
print(balance)
transistors = 1E+13
years = 26
transistors = transistors* 2**(year/2)
print(transistors)
num=8
print(num % 2)
num = 7
print(num % 2)
age = int(input"enter you dog's age: "))
human_age = age * 7 
print(human_age)

import random
num = random.randint(0,1) 
if num > 0.5:
  print('Heads')
else:
    print('Tails')
    
grade = 70
if grade > 60:
  print('You passed.')
else:
  print('You failed')

ph = int(input('Enter a ph value (0-14):'))
if ph > 7:
  print ('Basic.')
elif ph < 7:
  print ('Acidic.')
else:
  print('Neutral.')

import random 
question = input('Question:   ')
random_number = random.randint(1,9)
if random_number == 1:
  answer = 'yes - definitely'
elif random_number == 2:
  answer = 'it is decidely so'
elif random_number == 3:
  answer = 'without a doubt'
elif random_number == 4:
  answer = 'reply hazy, try again'
elif random_number == 5:
  answer = 'ask again later'
elif random_number == 6:
  answer = 'better not tell you now'
elif random_number == 7:
  answer = 'my sources say no' 
elif random_number == 8:
  answer = 'outlook not so good' 
elif random_number == 9:
  answer = 'very doubtful'
else:
  answer = 'Error'
print('magic 8 ball:' + answer)

height = int(input('what is your height (cm)?'))
credits = int(input('how many credits do you have?'))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits < 10:
  print("You are not tall wnough to ride.")
elif credits < 10 and height >= 137:
  print("You don't have enough credits")
else:
  print("You are not tall enough for this ride, nor you have credits")

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)



    
