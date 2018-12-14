import os

def createAccount():
        global username
        global password
        global initialDeposit
        username = str(input('Username: Create a username: '))
        password = int(input('Password: Enter your 4 digit PIN number: '))
        initialDeposit = float(input('Initial Deposit: Enter your initial deposit: '))

def login():
        username=str(input('Enter your username: '))
        file = open('./passwords.txt').read()
        file=file.split("\n")
        for n in file:
                data = n.split(" ")
                if username == data[0]:
                        password=int(input('Enter your 4 digit PIN password: '))
                        if password == data[1]:
                                print('Login Successful ')
                        elif password != data[1]:
                                print('Incorrect Password ')
                elif username != data[0]:
                        print('This username does not exist')
        
        
        


login()
