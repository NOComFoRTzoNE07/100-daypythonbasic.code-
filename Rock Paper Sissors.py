import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#my code
user_type = input("type 0 for rock, 1 for paper and 2 for scissors \n")
#user input
if user_type == "0":
  print(f"user input is: {rock}")
elif user_type == "1":
  print(f"user input is: {paper}")
elif user_type == "2":
  print(f"user input is: {scissors}")
else:
  print("Invalid Number")

#computer input
computer_input = random.randint(0, 2)
print(computer_input)

#winner
if user_type == computer_input:
  print("Draw")
  
elif user_type == "0" and computer_input == "1":
  print("Computer Wins")
  
elif user_type == "0" and computer_input == "2":
  print("User Wins")
  
elif user_type == "1" and computer_input == "0":
  print("User Wins")

elif user_type == "1" and computer_input == "2":
  print("Computer Wins")

elif user_type == "2" and computer_input == "0":
  print("Computer Wins")

elif user_type == "2" and computer_input == "1":
  print("User Wins")






