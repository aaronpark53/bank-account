import os

def createAccount():
        global username
        global password
        global initialDeposit
        username = input('Username: Create a username: ')
        password = str(input('Password: Enter your 4 digit PIN number: '))
        selectAccount()
        initialDeposit =input('Initial Deposit: Enter your initial deposit: ')
        f = open('passwords.txt', 'w')
        f.write(username+ ' ' +password+ ' ' +initialDeposit +'\n')
        
      

def login():
        username=str(input('Enter your username: '))
        file = open('./passwords.txt').read()
        file=file.split("\n")
        for n in file:
                data = n.split(" ")
                if data[0] == username:
                        password=int(input('Enter your 4 digit PIN password: '))
                        if password == data[1]:
                                print('Login Successful ')
                        elif password != data[1]:
                                print('Incorrect Password ')
                elif username != data[0]:
                        print('This username does not exist')

def selectAccount():
        x=input('Select Account:  1. Chequing   2. Savings ')
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)

createAccount()
        
