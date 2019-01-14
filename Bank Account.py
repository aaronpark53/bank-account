#Aaron Park and Damien Cheung
#December 12 2018 - January 11 2019
#Purpose: This is a bank account program. In this program, the user inputs
#all the information needed to run the program. This includes username,
#password, how much money they would like to deposit or withdraw, and what
#function they would like to use. This program has a file attatched to it
#that contains all the usernames, passwords, and the amount of money in
#the users accounts. This program contains many if/elif/else statements,
#functions for all the necessary options, and for and while loops. 




import os #this allows us to open and use our passwords file in the program

def start(): #this is the start function that will first appear when the program is ran. 
        print('Start: ')
        print('')
        y=True
        while y==True: #a while loop that will repeat until the user logs in or creates an account
                x=int(input('(1/2) 1. Create account  2. Login '))
                if x==1:
                      createAccount()
                      y=False
                elif x==2:
                      login()
                      y=False
                else:
                      print(x, 'was not an option idiot head dumb face stupid head')
                      print('Try again')
                      # an if/else/elif statement that the user uses to either log in or create an account
              
              

def createAccount():
        global username
        global password
        global chequingBalance
        global passwordLocation
        global savingsBalance #global variables that are used in other functions
        chequingBalance=0
        savingsBalance=0 #setting the balance of both accounts to 0.
        username = input('Create a username: ')
        password = str(input('Password: Enter your 4 digit PIN number: ')) #creating a username and password
        if len(password) != 4:
                print("That's not 4, can you count?????")
                start() #if the password is not 4 digits, the user will go back to the start screen
                return
        print('Make an initial deposit. Select an account: ')
        print('')
        x=int(input('(1/2):   1. Chequing  2. Savings '))
        print('')
        deposit=int(input('Input the value of your deposit in dollars: ')) #making an initial deposit for the user's account
        if x==1:
                chequingBalance= deposit
                print('Chequing balance: ', chequingBalance)
                savingsBalance=0 #making a deposit into a chequings account
        elif x==2:
                savingsBalance= deposit
                print('Savings balance: ', savingsBalance)
                chequingBalance=0 #making a deposit into a savings account
        else:
                print('Input unavailable. ') #this will show if the user does input 1 or 2
        f = open('passwords.txt', 'a') #opening the file
        f.write(username+ ' ' +password+ ' ' +str(chequingBalance) + ' ' + str(savingsBalance) + '\n') #this adds all their information to the passwords file
        f.close()

        file = open('./passwords.txt').read()
        file=file.split("\n")[:-1]
        passwordLocation = len(file)-1
        return #returning to the options function
                                  

def login():
        global chequingBalance
        global savingsBalance
        global username
        global password
        global passwordLocation #global variables that are used in other functions
        file = open('./passwords.txt').read()
        file=file.split("\n")
        login=True
        password=True #setting up while loops
        x=3 #this is here so that the user only has four tries to log in 
        while login==True:
                while x>=0:
                        username=str(input('Enter your username: ')) #where the user inputs their username
                        userFound = False
                        for passwordLocation in range(len(file)):
                                data = file[passwordLocation].split(" ")
                                if data[0] == username: #data[0] is the column where all the usernames are kept. this also checks if the user input is a real username
                                        userFound = True
                                        while password==True and x>0:
                                                password=input('Enter your 4 digit PIN password: ') #where the user inputs their password  is the column where all the usernames are kept. this also checks if the user input is a real username
                                                if password == data[1]: #data[1] is the column where all the passwords are kept. this also checks if the user input is the right password. 
                                                        print('Login Successful ')
                                                        password=False
                                                        login=False
                                                        chequingBalance= float(data[2]) #data[2] is the column where the chequing balance is kept
                                                        savingsBalance= float(data[3]) #date[3] is the column where the savings balance is kept.
                                                        username= data[0]
                                                        password= data[1]
                                                        return
                                                elif password != data[1]: #if the password entered does not match up to the one in the file associated with their username they will re-enter their password
                                                        print('Incorrect Password ')
                                                        print('Re-enter your password')
                                                        password=True
                                                        x-=1
                        if userFound == False:
                                print('This username does not exist') #this will show if the input does not match up any of the usernames in the file.
                                x-=1  

def option(): #this is the main function of the program, it directs the user to all the different function they can use in a bank account.
        x=True
        while x==True:
                print('What would you like to do?')
                print('''1. Withdraw
2. Deposit
3. Transfer Money
4. Print Balance
5. Logout''')
                y=int(input('--->'))
                if y==1:
                        withdraw()
                elif y==2:
                        deposit()
                elif y==3:
                        transferMoney()
                elif y==4:
                        printBalance() #series of if/elif statements that the user uses to decide what to do.
                elif y==5:
                        print('Thank you for banking with the Bank') 
                        break #this break is used to log out
                else:
                        print(y,'was not an option idiot head dumb face stupid head') 

def withdraw():
        global chequingBalance
        global savingsBalance #global variables that are used in other functions
        global passwordLocation
        n=True
        while n==True:
                x=int(input('''Select account to withdraw from:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3): ''')) #this is where the user selects which account they want to withdraw money
                if x==1:
                        withdrawal=float(input('Input value of the withdrawal: '))
                        if withdrawal <= chequingBalance: #if they withdrew less money than they have in their account, the program will continue
                                print('Current Chequing account balance: ', chequingBalance)
                                chequingBalance= chequingBalance - withdrawal
                                update() #updating their chequing balance
                                print('New Chequing account balance: ', chequingBalance)
                                print('You have successfully withdrawn ', withdrawal, ' dollars') 
                                return #printing their new chequing balance and returning the user to the options menu
                        else:
                                print('Insufficient Funds.')
                                return #this will show if the user tries to steal money from the bank and withdraw more money than they have, and return them to the options main menu.
                elif x==2:
                        withdrawal=int(input('Input value of the withdrawal: '))
                        if withdrawal <= savingsBalance:
                                print('Current Savings account balance: ', savingsBalance)
                                savingsBalance= savingsBalance - withdrawal
                                update()
                                print('New Savings account balance: ', savingsBalance)
                                print('Your deposit of: ', withdrawal, 'dollars was successful')
                                return #same thing but for savings account
                        else:
                                print('Insufficient Funds.')
                                return
                elif x==3:
                        n=False
                        return #if they choose 3, they will go back to the options menu
                else:
                        print('That is not an option. Try again. ') #this will print if the user does not input 1, 2, or 3 
                

def deposit():
        global chequingBalance
        global savingsBalance #global variables that are used in other functions
        global passwordLocation
        n=True
        while n==True:
                x=int(input('''Select account to deposit into:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3):  ''')) #this is where the user selects which account they want to deposit money to
                if x==1:
                        print('Current Chequing account balance: ', chequingBalance)
                        deposit=float(input('Input the value of your deposit: ')) #where the user inputs their deposit
                        chequingBalance=chequingBalance+deposit
                        update() #updating their chequing balance
                        print('New Chequing account balance: ', chequingBalance)
                        print('Your deposit of ', deposit, 'dollars was successful.') 
                        return #printing their new chequing balance and returning the user to the options menu
                elif x==2:
                        print('Current Savings account balance: ', savingsBalance)
                        deposit=float(input('Input the value of your deposit: '))
                        savingsBalance=savingsBalance+deposit
                        update()
                        print('New Savings account balance: ', savingsBalance)
                        return #same thing for savings account
                elif x==3:
                        n=False
                        return #if they choose 3, they will go back to the options menu
                else:
                        print('That is not an option. Try again.') #this will print if the user does not input 1, 2, or 3


def transferMoney(): #this is a function that allows you to transfer money between your own chq/sav accounts
        global chequingBalance 
        global savingsBalance #these global statements allow you to use these variables outside of the function
        x=int(input('''Select option:
1. Chequing to Savings 
2. Savings to Chequing 
3. Go Back             
Enter(1/2/3):  ''')) #x is the variable that represents the users choice and it will correspond with the correct option which is displayed with the print statement
        if x==1:
                print('Current Chequing account balance: ',chequingBalance)
                print('Current Savings account balance: ', savingsBalance) #displaying the current accounts balance
                transferAmount=float(input('Input the value of the transfer: ')) #input for the amount of money that is going to be transferred
                if transferAmount > chequingBalance:
                        print('Insufficient funds. ')
                        return #if the transfer amount is more than the user owns in the account that is transferring money, the program will say that there is insufficient funds and it will relaunch the option
                else:
                        chequingBalance= chequingBalance-transferAmount #if the amount is acceptable, the chequing balance will lose that amount of money and the savings account will gain that money, simulating the transfer between accounts.
                        savingsBalance=savingsBalance+transferAmount
                        update() #update file function
                        print('You have successfully transferred ', transferAmount, 'from Chequings to Savings.')
                        print('''
New Chequing account balance: ''', chequingBalance)
                        print('New Savings account balance: ', savingsBalance)
                        return #a few print statements that explain what happened, then return to options menu.
        elif x==2:
                print('Current Savings account balance: ', savingsBalance)
                print('Current Chequing account balance: ', chequingBalance)
                transferAmount=float(input('Input the value of the transfer: '))
                return
                if transferAmount > savingsBalance:
                        print('Insufficient funds. ')
                        return
                else:
                        chequingBalance= chequingBalance+transferAmount
                        savingsBalance=savingsBalance-transferAmount
                        update()
                        print('You have successfully transferred ', transferAmount, 'from Savings to Chequing.')
                        print('''
New Savings account balance: ''', savingsBalance)
                        print('New Chequing account balance: ', chequingBalance)
                        return #the same coding but reversed for the savings to chq option rather than cheq to savings
        elif x==3:
                return #if the user wants to go back, the options menu will appear
        else:
                print('That is not an option. ') #if the user doesnt input 1/2/3, this message appears
                
def printBalance(): #function that will allow the user to check their account balances

        x=int(input('Select Account(1/2):  1. Chequing   2. Savings ')) #displaying the options 
        if x == 1:
                print(chequingBalance) #if the user enters 1, the chequing balance will be displayed
        elif x == 2:
                print(savingsBalance) #if 2 is entered, savings balance is displayed


                

def update(): #this is a function that updates the info in the passwords file and removes the old information
        global passwordLocation #this variable is open to use in other coding
        file = open('./passwords.txt').read() #the code opens the passwords file and reads it
        file=file.split("\n")[:-1] #file is split and read in new lines so that each accounts information is seperately stored

        f = open('passwords.txt', 'w') #the file is opened and is permitted to write over

        for n in range(len(file)):
                if n == passwordLocation:
                        continue #continue if the scan finds the correct password location (which is stored in an earlier function (create accoutn/login))
                f.write(file[n] + '\n') #a new line is written
        
        f.write(username+ ' ' +password+ ' ' +str(chequingBalance) + ' ' + str(savingsBalance) + '\n')
        f.close() #all the updated account data is written into the newest line then the file is closed

        passwordLocation = len(file)-1 # the new location is updated
                





print('Welcome to the Bank. ') #opening statement
start() #launching the start function. If it is successfully completed,
option() #the options menu will launch and run continuously until the user logout


