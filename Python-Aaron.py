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
        
def initialDeposit():
        print('Make an iniital deposit: ')
        print('Select an account for the initial deposit: ')
        x=input('1. ')

        
def selectAccount():
        x=input('Select Account:  1. Chequing   2. Savings ')
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)

login()
print('x')
