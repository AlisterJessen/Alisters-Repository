from random import randint
from time import sleep
john = input("This is a typing speed test, you are going to be given a random text out of three texts and your job is to copy it as fast as you can. you start afer the countdown ")

rt = randint(1, 3)
print("Random Text: " + rt)

number = 5
while number > 0:
    print(number)
    number = number - 1
    sleep(1)
print("Start!")



t1 = "This should show the user some text, and then challenge them to type it"
t2 = "hello"
t3 = "three"

if (rt == 1):
    t1a = input(t1)

if (t1a == t1):
    print("correct ")

if (t1a != t1):
    print("try again, The text was '" + t1 + "' and you answer was '" + t1a + "'")



if (rt == 2):
    t2a = input(t2)

if (t2a == t2):
    print("Correct ")



if (rt == 3):
    t3a = input(t3)

