import random

def print_des(i):
    if i==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif i==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif i==2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("What do you choose?")
c = int(input("0 for rock, 1 for paper and 2 for scissor\n"))
print_des(c)

d = random.randint(0,2)
print("Computer chose:")
print_des(d)

if c == d:
    print("Draw!")
elif (c == 0 and d == 1) or (c == 1 and d == 2) or (c == 2 and d == 0):
    print("You Lose!")
else:
    print("You Win!")