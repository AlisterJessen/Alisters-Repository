
from random import randint


number = int(input("choose the range of numbers: "))
print(number)

for i in range(1):
    answer = randint(1, number)

print(answer)


guess = int(input("Guess the number: "))

if number==answer:
    print("Correct")

if number>answer:
    print("to high")

if number<answer:
    print("to low")