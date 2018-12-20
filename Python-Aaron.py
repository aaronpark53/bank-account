#Aaron Park and Damien Cheung
#December 10 2018 to January 18 2019
#This is a banking program we made for our culminating task. The program will be able to create an account, login, withdraw and deposit money





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

        
def selectAccount():
        x=input('Select Account:  1. Chequing   2. Savings ')
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)


def option():
        x=True
        while x==True:
                print('What would you like to do?')
                print('1. Withdraw, 2. Deposit, 3. Transfer Money, 4.E-transfer, 5.Logout')
                y=int(input('--->'))
                y=y.upper()
                if y==1:
                        withdraw()
                elif y==2:
                        deposit()
                elif y==3:
                        transferMoney()
                elif y==4:
                        e-transfer()
                elif y==5:
                        print('Thank you for banking with bank')
                        print('Bye bye now *waving hand*')
                        break
                elif y>5:
                        print(
        







login()
print('x')
