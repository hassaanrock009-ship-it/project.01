


import random
number_to_guess=random.randint(1,100)
while True:
 try:
  guess=int(input("enter the number you want to guess"))
  if guess < number_to_guess:
    print("too low!")
  elif guess> number_to_guess:
     print("Too high")
  else:
     print("COngratulations!You have guessed the number")  
     break  
 except ValueError:
    print("Please Enter a valid number")
 if guess < number_to_guess:
    print("too low")
    


        
        