import os

def start():
        print('Start: ')
        print('')
        x=int(input('(1/2) 1. Create account  2. Login '))
        if x==1:
              createAccount()
        elif x==2:
              login()
        else:
              print(x, 'was not an option')
              

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
        username=str(input('Enter your username: '))
        file = open('./passwords.txt').read()
        file=file.split("\n")
        for n in file:
                data = n.split(" ")
                if data[0] == username:
                        
                        password=input('Enter your 4 digit PIN password: ')
                        if password == data[1]:
                                print('Login Successful ')
                        elif password != data[1]:
                                print('Incorrect Password ')
                elif username != data[0]:
                        print('This username does not exist')


def initialDeposit():
        print('Make an initial deposit. Select an account: ')
        print('')
        x=input('(1/2):   1. Chequing  2. Savings ')
        print('')
        deposit=int(input('Input the value of your deposit in dollars: '))
        if x==1:
                chequingBalance= deposit
                print('Chequing balance: ')
                print(chequingBalance)
        elif x==2:
                savingsBalance= deposit
                print('Savings balance: ')
                print(savingsBalance)

        
def selectAccount():
        x=input('Select Account(1/2):  1. Chequing   2. Savings ')
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)
              
start()
