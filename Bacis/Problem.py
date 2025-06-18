import random

player=input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissor\n\n")
computer=random.choice("123")
print('you choose'+player+".")
print('computer turn'+computer+".")

if(player=="1" and computer=="3"):
    print("you win")
elif(player=="2" and computer=="1"):
    print("you win")
elif(player=="3" and computer=="2"):
    print("you win")
elif(player==computer):
    print("tie game")