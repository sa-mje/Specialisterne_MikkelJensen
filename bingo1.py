import random

def print_plate(title,plateMatrix):
    #Print single plate:
    print("\n" + title,end = "")
    j=0
    while j<3:
        print("\n|",end = "")
        i=0
        while i<9:
            if plateMatrix[i][j]==0: #Empty if 0
                print("  |",end = "")
            elif plateMatrix[i][j]//10==0: #Add extra space if single digit
                print(" ",end = "")
                print(plateMatrix[i][j],end = "")
                print("|",end = "")
            else:
                print(plateMatrix[i][j],end = "")
                print("|",end = "")
            i+=1
        j+=1

def int_input(prompt):
    #Get integer input
    while True:
        try:
            intnum = int(input(prompt))
            return intnum
        except ValueError:
            print('Not a proper integer! Try again')

def generate_single_plate():
    #Generates a single bingo plate while making sure there is 1-2 per column
    bingoplate=[]
    numbersOnPlate=0
    numbersColumnList=[0,0,0,0,0,0,0,0,0] #List for the number of elements in each column
    emptyColumns=9
    
    while numbersOnPlate<15:
        #Get random number
        num=random.randint(1, 90)
        addToPlate=True #Changed to False if number doesn't pass checks
        
        #Check if it is on the plate already
        if numbersOnPlate!=0:
            i=0
            while i<numbersOnPlate:
                if num==bingoplate[i]:
                    addToPlate=False
                i+=1
        
        #Check it does not give a 3rd value in a column
        numColumn=num//10 #Column index so from 0-8
        if numColumn==9: #In case if 90 should be in last column
            numColumn=8
        
        if numbersColumnList[numColumn]==2:
            continue
        
        #Check if number have to be in a critical column to avoid empty columns
        if 15-numbersOnPlate<=emptyColumns and numbersColumnList[numColumn]!=0:
            continue
        
        if addToPlate==False:
            continue
        
        #Add number to bingo plate
        bingoplate.append(num)
        numbersOnPlate+=1
        if numbersColumnList[numColumn]==0:
            emptyColumns-=1
        numbersColumnList[numColumn]+=1
        
    #Sort numbers in bingo plate list
    bingoplate.sort()
    
    #Create matrix
    matrix=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    i=0
    while i<15:
        numColumn=bingoplate[i]//10 #Column index so from 0-8
        if numColumn==9: #In case if 90 should be in last column
            numColumn=8
        
        if numbersColumnList[numColumn]==1:
            #If only element in row just
            pos=random.randint(0, 2)
            matrix[numColumn][pos]=bingoplate[i]
        elif numbersColumnList[numColumn]==2:
            #If two elements, pos is here position of hole
            pos=random.randint(0, 2)
            if pos==0: #Empty space top
                matrix[numColumn][1]=bingoplate[i]
            elif pos==1 or pos==2: #Empty space middle or bottom
                matrix[numColumn][0]=bingoplate[i]
            numbersColumnList[numColumn]+=1
        elif numbersColumnList[numColumn]==3:
            if pos==0 or pos==1: #Empty space top or middle
                matrix[numColumn][2]=bingoplate[i]
            elif pos==2: #Empty space bottom
                matrix[numColumn][1]=bingoplate[i]
        else:
            print('Error in number of elements in column.')
        i+=1
    
    #Return plate
    return bingoplate,matrix

def generate_bingo_plates(plateName,n):
    #Generates a list of unique bingo plates
    bingolist = []
    matrixlist = []
    while n>0:
        #Generate single plate
        tempPlate,tempMatrix=generate_single_plate()
        addToList=True
        
        #Check it is unique
        i=0
        while i<len(bingolist):
            if tempPlate==bingolist[i]:
                addToList=False
            i+=1
        
        if addToList==False:
            continue
        
        #Add to bingolist and repeat
        bingolist.append(tempPlate)
        matrixlist.append(tempMatrix)
        n-=1
    
    return plateName,bingolist,matrixlist


print('Welcome to Bingo!')
plateName=input('Title of plates: ')
n=int_input('Number of plates to be generated: ')
plateName1,bingolist1,matrixlist1=generate_bingo_plates(plateName,n)
#Print plates
i=0
while i<n:
    print_plate(plateName1,matrixlist1[i])
    i+=1
