import os

def start():
        print('Start: ')
        print('')
        y=True
        while y==True:
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
              
              

def createAccount():
        global username
        global password
        global chequingBalance
        global savingsBalance

        chequingBalance=0
        savingsBalance=0
        username = input('Username: Create a username: ')
        password = str(input('Password: Enter your 4 digit PIN number: '))
        print('Make an initial deposit. Select an account: ')
        print('')
        x=int(input('(1/2):   1. Chequing  2. Savings '))
        print('')
        deposit=int(input('Input the value of your deposit in dollars: '))
        if x==1:
                chequingBalance= deposit
                print('Chequing balance: ', chequingBalance)
                savingsBalance=0
        elif x==2:
                savingsBalance= deposit
                print('Savings balance: ', savingsBalance)
                chequingBalance=0
        else:
                print('Input unavailable. ')
        f = open('passwords.txt', 'a')
        f.write(username+ ' ' +password+ ' ' +str(chequingBalance) + ' ' + str(savingsBalance) + '\n')
        
      

def login():
        file = open('./passwords.txt').read()
        file=file.split("\n")
        login=True
        password=True
        x=3
        while login==True:
                while x>=0:
                        for n in file:
                                data = n.split(" ")
                                username=str(input('Enter your username: '))
                                if data[0] == username:
                                        while password==True:
                                                password=input('Enter your 4 digit PIN password: ')
                                                if password == data[1]:
                                                        print('Login Successful ')
                                                        password=False
                                                        login=False
                                                        return
                                                elif password != data[1]:
                                                        print('Incorrect Password ')
                                                        print('Re-enter your password')
                                                        password=True
                                                        x-=1
                                else:
                                        print('This username does not exist')
                                        x-=1

        
def printBalance():
        x=input('Select Account(1/2):  1. Chequing   2. Savings ')
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)

def withdraw():
        global chequingBalance
        global savingsBalance
        n=True
        while n==True:
                x=int(input('''Select account to withdraw from:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3): '''))
                if x==1:
                        deposit=float(input('Input value of the withdrawal: '))
                        if deposit <= chequingBalance:
                                chequingBalance= chequingBalance - deposit
                                print(chequingBalance)
                        else:
                                print('Insufficient Funds.')
                elif x==2:
                        deposit=int(input('Input value of the withdrawal: '))
                        if deposit <= savingsBalance:
                                savingsBalance= savingsBalance - deposit
                                print(savingsBalance)
                        else:
                                print('Insufficient Funds.')
                elif x==3:
                        n=False
                        break
                else:
                        print('That is not an option. Try again. ')
                

def deposit():
        global chequingBalance
        global savingsBalance
        x=int(input('''Select account to deposit into:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3):  '''))
        if x==1:
                print('Current Chequing account balance: ', chequingBalance)
                deposit=float(input('Input the value of your deposit: '))
                chequingBalance=chequingBalance+deposit
                print('New Chequing account balance: ', chequingBalance)
        elif x==2:
                print('Current Savings account balance: ', savingsBalance)
                deposit=float(input('Input the value of your deposit: '))
                savingsBalance=savingsBalance+deposit
                print('New Savings account balance: ', savingsBalance)

def transfer():
        global chequingBalance
        global savingsBalance
        x=int(input('''Select option:
1. Chequing to Savings 
2. Savings to Chequing 
3. Go Back             
Enter(1/2/3):  '''))
        if x==1:
                print('Current Chequing account balance: ',chequingAccount)
                print('Current Savings account balance: ', savingsAccount)
                transferAmount=float(input('Input the value of the transfer: '))
                
start()
withdraw()
transfer()
        



