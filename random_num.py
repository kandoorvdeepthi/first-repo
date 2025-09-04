import random

number_to_guess=random.randint(1,100)
while True:
 try:
  guess=int(input('enter a number of your choice between 1 and 100: '))
  if guess<number_to_guess:
   print('too low!')
  elif guess>number_to_guess:
   print('too high!')
  else:
   print('yeah!!!! you guessed it correct')
   break
 except ValueError:
  print('invalid input')

#import random

#number_to_guess=random.randint(1,100)
#while True:
# try:
#  guess=int(input('enter a number between 1 and 100: '))
#  if guess<number_to_guess:
#   print('too low!')
#  elif guess>number_to_guess:
#   print('too high!')
#  else:
#   print('yeah!!! you guessed right')
#   break
# except ValueError:
#  print('please enter a valid number')