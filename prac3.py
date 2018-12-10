# 1
import random

def guess(number):
    answer = random.randint(0, number + 1)
    print("Now, you just entered the range of number(0 to you entered number)."
          "You can guess the number from the range of number")
    guess = int(input("Please guess the number:"))
    if guess < answer:
        print("it's too little!")
    elif guess > answer:
        print("Sorry, it's a little big.")

    while guess != answer:
        newguess = int(input("I believe you can guess right. Let's do it again.:"))
        if newguess == answer:
            print("WOW!Congratulations")
            break
        elif newguess < answer:
            print("it's too little!")
        else:
            print("Sorry, it's a little big.")

player = input("Hi, What's your name?")
print("Hello " + player + ", Let's begin the game." )
num = int(input("Please input a positive number:"))
if num < 0:
    newNum = int(input("Sorry," + player + ", We need you to print a positive number, please input again:"))
    guess(newNum)
else:
    guess(num)

# 2
print('There are 3 numbers，please Guess what it is.')
print('The clue I gave is:')
print('When I say:                     It means:')
print('error                           The 3 numbers are not in the mystical numbers.')
print('Only the number is correct      the number is right , but the position is not right..')
print('Absolutely right                numbers is right and the position also right.')


def judge(guess,answers):
    if guess == answers:
        return "Congratulations! YOU WIN!"
    tips = []
    for i in range(len(answers)):
        if guess[i] == answers[i]:
            tips.append("Absolutely right")
        elif guess[i] != answers[i] and guess[i] in answers:
            tips.append("Only the number is correct")
        else:
            tips.append("error")
    return tips

print("Let's begin the game! ")
print("Remember, You only hava max 10 times to guess!")
while True:
    guessTimes = 1
    numbers = random.sample(range(0, 9), 3)
    #print(numbers)
    while guessTimes <= 10:
        print("This is the " + str(guessTimes) + " times:")
        guessNum = input("Please input the 3 numbers you guess:")
        guesslist = []
        for i in range(len(guessNum)):
            guesslist.append(int(guessNum[i]))
        #print(guesslist)
        print(judge(guesslist,numbers))

        if guesslist == numbers:
            break

        if guessTimes > 10:
            print("I'm sorry. YOU LOSE! The answer is " + str(numbers))
        guessTimes += 1

    again = input("Do you want to play again? Y or N")
    if again == "N":
        break

# 3
from tkinter import *

top = Tk()
list1 = ['C', 'python', 'php', 'html', 'SQL', 'java']

listb = Listbox(top)
for item in list1:
    listb.insert(0,item)
listb.pack()


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(top, text = "CSS", variable = CheckVar1,
                 onvalue = 10, offvalue = 20, height=2,
                 width = 10)
C2 = Checkbutton(top, text = "jQuery", variable = CheckVar2,
                 onvalue = 20, offvalue = 10, height=2,
                 width = 10)
C1.pack()
C2.pack()

B = Button(top, text="clickme")
B.pack()

top.mainloop()