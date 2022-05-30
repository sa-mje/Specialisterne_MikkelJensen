import random

#Generate list with random integers from 1 to 6 with length n:
def generate_random_code(n):
    codelist = []
    while n>0:
        codelist.append(random.randint(1, 6))
        n-=1
    return codelist

#Get integer input
def int_input(prompt):
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print('Not a proper integer! Try again')

#Get list of digits from integer
def int_split_to_list(num,n):
    #Generate list of 0's with length n:
    i=0
    numlist=[]
    while i<n:
        numlist.append(0)
        i+=1
    #Transform integer num to list of digits:
    j=n-1
    while j>=0:
        numlist[j]=num%10
        num=num//10
        j-=1
    return numlist

#Get string of colors from list of digits
def list_to_color_str(guesslist,n):
    switcher = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue", 5: "White", 6: "Black"}
    color_str=""
    i=0
    while i<n:
        color_str += switcher.get(guesslist[i], "NoColor") + " "
        i+=1
    return color_str

print('Welcome to MASTERMIND!')
while True: #Break this loop when exiting game
    #Initial values
    n=4 #Number of pegs, default = 4
    round=1 #Guesses used so far of the 12
    guessnum=0
    codelist=generate_random_code(n)
    #Starttext
    print('A new game has been started. A secret code with',n,'pegs has been generated.')
    print('The inputs should be given as numbers from 1 to 6 without spaces and then press enter. The following digits correspond to the following numbers:')
    print('1=Red,2=Yellow,3=Green,4=Blue,5=White,6=Black')
    print('For testing only; The secret code is:', codelist)

    while round<=12:
        #Get guess from user input and check it:
        continue_input=True
        while continue_input:
            continue_input=False
            #Get input
            guessnum = int_input('Guess ' + str(round) + ' input: ')
            #Check length
            if len(str(guessnum))!=n:
                print('Input not',n,'digits long! Try again')
                continue_input=True
                continue
            #Make list of digits
            guesslist = int_split_to_list(guessnum,n)
            #Check digits between 1 and 6
            i=0
            while i<n:
                if guesslist[i]!=1 and guesslist[i]!=2 and guesslist[i]!=3 and guesslist[i]!=4 and guesslist[i]!=5 and guesslist[i]!=6:
                    print('Input digits not between 1 and 6! Try again')
                    continue_input=True
                i+=1


        #Check number of black dots:
        black=0
        i=0
        while i<n:
            if guesslist[i]==codelist[i]:
                black+=1
            i+=1

        #Checknumber of white dots:
        white=0
        i=0
        while i<n:
            j=0
            while j<n:
                if guesslist[i]==codelist[j] and guesslist[i]!=codelist[i]:
                    white+=1
                    break
                j+=1
            i+=1
        #print('White dots: ', white)

        #Print round results:
        print_str=list_to_color_str(guesslist,n) + '| '
        i=black
        while i>0:
            print_str=print_str+'Black '
            i-=1
        i=white
        while i>0:
            print_str=print_str+'White '
            i-=1
            
        print(print_str)
        #Check if player input is the code:
        if black==n:
            break
        round+=1
    
    #Check if player has won or lost the game:
    if round<=12:
        print('You win!')
    else:
        print('You lose! The secret code was: ', codelist)
 
    #Do the player want to play a new round?
    end=False
    while True:
        #Get input from player:
        cont=int_input('\nWanna play a new round (1=yes and 0=no)?: ')
        if cont==1:
            end=False
            break
        elif cont==0:
            end=True
            break
        else:
            print('Only 1 or 0 is allowed.')
    #Check if the game should end:
    if end==True:
        break
