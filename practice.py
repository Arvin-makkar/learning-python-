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

rating = 4.7
if rating > 4.5:
  print('perfection')
elif rating > 4:
  print('excellent')
elif rating > 3:
  print('good')
elif rating > 2:
  print('fair')
else:
  print('poor')

grade = int(input('enter your grate level:'))
if grade == 9:
  print('freshman')
elif grade == 10:
  print('sophomore')
elif grade == 11:
  print('junior')
elif grade == 12:
  print('senior')
else:
  print('TBD')

import random
fact = random.randint(1,6)
if fact == 1:
  print('Flamingos turn pink by eating shrimp.')
elif fact == 2:
  print('Honey never goes bad.')
elif fact == 3:
  print('Shrimp can only swim backwards.')
elif fact == 4:
  print('A taste bud\'s life is about 10 days.')
elif fact == 5:
  print('You can\'t sneeze while sleeping.')
else:
  print('Tiny pocket in jeans was for watches.')

month = int(input('enter month number:'))
if month == 1 or month == 2 or month == 3:
  print('Winter 🌨️')
elif month == 4 or month == 5 or month == 6:
  print('Spring 🌱')
elif month == 7 or month == 8 or month == 9:
  print('Summer 🌻')
elif month == 10 or month == 11 or month == 12:
  print('Autumn 🍂')
else:
  print('Invalid')

earth_weight = float(input('enter your weight:'))
planet = int(input('enter the planet number:'))
destination_weight = earth_weight * 0.38
if planet == 1:
  destination_weight = earth_weight * 0.38
  print('destination_weight')
elif planet == 2:
  destination_weight = earth_weight * 0.91
  print('destination_weight')
elif planet == 3:
  destination_weight == earth_weight * 0.38
  print('destination_weight')
elif planet == 4:
  destination_weight = earth_weight * 2.53
  print('destination_weight')
elif planet == 5:
  destination_weight = earth_weight * 1.07
  print('destination_weight')
elif planet == 6:
  destination_weight = earth_weight * 0.89
  print('destination weight')
elif planet == 7:
  desstination_weight = earth_weight * 1.14
  print('destination_weight')
else:
  print('invalid number')    

print('BANK OF CODÉDEX')
pin = int(input('Enter your PIN: '))
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))
if pin == 1234:
  print('PIN accepted!')

guess = 0
tries = 0
while guess != 6 and tries < 5:
  guess = int(input('guess the number:'))
  #update tries
print(" you got it!")

for i in range(100):
  print('I will not throw airplanes in class room')

for x in range(99 , 0 , -1):
  print(f'{x} bottles of beer on the wall')
  print(f'{x} bottles of beer')
  print('take one down, pass it around')
  print(f'{x-1} bottles of beer on the wall')

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
  elif num % 3 == 0:
      print('fizz')
  elif num % 5 == 0:
      print('buzz')
  else:
      print(num)

answer = input('are we there yet?')
while answer != 'yes':
  answer = input('are we there yet?')

for i in range(10,0,-1):
  print(i)
print('Happy New Year! 🥳')

import random
# 1. roll the two die for the first time
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2

# 2. keep loopint while the total is not 2
while total != 2:
  print('nope')
  # reroll the die inside the loop to update the total 
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
  # 3 print the success message once the loop stops 
  print('snake eye!')

for i in range(1,25):
  print('* '* i)

# 1. ask the user for an integer and store it 
number = int(input('enter a number:'))
# 2. define a total variable with an identical value of 0 
total = 0
# 3. use a for loop to calculate the total of the squares 
for i in range(1, number + 1):
  total += i ** 2
# 4. print the final integer output
print(total)


# Storing grades in a class

hw_grade1 = 98
hw_grade2 = 87
hw_grade3 = 92
hw_grade4 = 96

quiz_grade1 = 9
quiz_grade2 = 6
quiz_grade3 = 8

# Storing grades in a class

hw_grades = [98, 87, 92, 96]
quiz_grades = [9, 6, 8]

temp = [86, 80, 82, 87, 79, 80, 82]
ph = [7.2, 7.1, 7.0, 7.0, 7.2, 7.1]
now_playing = ['Barbie', 'Oppenheimer', 'Talk to Me', 'Blue Beetle']


grocery = ['🥚 Eggs','🥑 Avocados','🍪 Cookies','🌶 Hot Pepper Jam','🫐 Blueberries','🥦 Broccoli']
print(grocery)

todo = ['🏦 Get quarters.','🧺 Do laundry.','🌳 Take a walk.','💈 Get a haircut.','🍵 Make some tea.','💻 Complete Lists chapter.','💖 Call mom.','📺 Watch My Hero Academia.'  ]
print(todo[0])
print(todo[1])

print(todo[2:5])
print(todo[5])   #this should given an index error


lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]
print(min(lego_parts))
print(max(lego_parts))

books = [
    'Harry Potter',
    '1984',
    'The Fault in Our Stars',
    'The Mom Test',
    'Life in Code'
]

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)

playlist = ["kesariya","heeriye","apna bana le","satranga","chaleya"] 
print(playlist)

things_to_do = ["travel to japan",
"become a python developer",
"build my own app"]
print(things_to_do)


