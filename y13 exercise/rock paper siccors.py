from random import randint

uc = int(input("Rock(1), Paper(2), Scissors(3) shoot: "))


cc = randint(1, 3)
print(cc)


if (uc == 1 and cc == 3) or (uc == 2 and cc == 1) or (uc == 3 and cc == 2):
    print("User Wins")


if (cc == 1 and uc == 3) or (cc == 2 and uc == 1) or (cc == 3 and uc == 2):
    print("computer Wins")

if (cc == 1 and uc == 1) or (cc == 2 and uc == 2) or (cc == 3 and uc == 3):
    print("Tie")