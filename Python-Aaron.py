#Aaron Park and Damien Cheung
#December 10 2018 to January 18 2019
#This is a banking program we made for our culminating task. The program will be able to create an account, login, withdraw and deposit money





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
        exists = False
        x=3
        while login==True:
                while x>=0:
                        username=str(input('Enter your username: '))
                        for n in file:
                                data = n.split(" ")
                                if data[0] == username:
                                        exists = True
                                        while password==True and x>0:
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
                        if exists == False:
                                print('This username does not exist')
                                x-=1

        

def option():
        x=True
        while x==True:
                print('What would you like to do?')
                print('1. Withdraw, 2. Deposit, 3. Transfer Money, 4.E-transfer, 5.Logout')
                y=int(input('--->'))
                if y==1:
                        withdraw()
                elif y==2:
                        deposit()
                elif y==3:
                        transfer()
                elif y==4:
                        eTransfer()
                elif y==5:
                        print('Thank you for banking with bank')
                        print('Bye bye now *waving hand*')
                        break
                elif y>5:
                        print(y,'was not an option idiot head dumb face stupid head')
        

def printBalance():
        x=input('Select Account(1/2):  1. Chequing   2. Savings ')
        if x == 1:
                print(data[2])
        elif x == 2:
                print(data[3])



def withdraw():
        file = open('./passwords.txt').read()
        file=file.split("\n")
        for n in file:
                        data = n.split(" ")
                        n=True
                        while n==True:
                                x=int(input('''Select account to withdraw from:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3): '''))
                                if x==1:
                                        withdrawal=float(input('Input value of the withdrawal: '))
                                        if withdrawal <= int(data[2]):
                                                print('Current Chequing account balance: ', data[2])
                                                data[2]= int(data[2]) - withdrawal
                                                print('New Chequing account balance: ', data[2])
                                                print('You have successfully withdrawn ', withdrawal, ' dollars')
                                                return
                                        else:
                                                print('Insufficient Funds.')
                                elif x==2:
                                        withdrawal=int(input('Input value of the withdrawal: '))
                                        if withdrawal <= int(data[3]):
                                                print('Current Savings account balance: ', data[3])
                                                data[3]= int(data[3]) - withdrawal
                                                print('New Savings account balance: ', data[3])
                                                print('Your deposit of: ', withdrawal, 'dollars was successful')
                                                return
                                        else:
                                                print('Insufficient Funds.')
                                elif x==3:
                                        n=False
                                        return
                                else:
                                        print('That is not an option. Try again. ')


def deposit():
        
        x=int(input('''Select account to deposit into:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3):  '''))
        if x==1:
                print('Current Chequing account balance: ', data[2])
                deposit=float(input('Input the value of your deposit: '))
                data[2]=data[2]+deposit
                print('New Chequing account balance: ', data[2])
        elif x==2:
                print('Current Savings account balance: ', data[3])
                deposit=float(input('Input the value of your deposit: '))
                data[3]=data[3]+deposit
                print('New Savings account balance: ', data[3])




def transfer():
        
        x=int(input('''Select option:
1. Chequing to Savings 
2. Savings to Chequing 
3. Go Back             
Enter(1/2/3):  '''))
        if x==1:
                print('Current Chequing account balance: ',data[2])
                print('Current Savings account balance: ', data[3])
                transferAmount=float(input('Input the value of the transfer: '))
                if transferAmount > data[2]:
                        print('Insufficient funds. ')
                else:
                        data[2]= data[2]-transferAmount
                        data[3]=data[3]+transferAmount
                        print('You have successfully transferred ', transferAmount, 'from Chequings to Savings.')
                        print('''
New Chequing account balance: ''', data[2])
                        print('New Savings account balance: ', data[3])
        elif x==2:
                print('Current Savings account balance: ', data[3])
                print('Current Chequing account balance: ', data[2])
                transferAmount=float(input('Input the value of the transfer: '))
                if transferAmount > data[3]:
                        print('Insufficient funds. ')
                else:
                        data[2]= data[2]+transferAmount
                        data[3]=data[3]-transferAmount
                        print('You have successfully transferred ', transferAmount, 'from Savings to Chequing.')
                        print('''
New Savings account balance: ''', data[3])
                        print('New Chequing account balance: ', data[2])



def eTransfer():
        file = open('./passwords.txt').read()
        file=file.split("\n")
        y=True
        while y==True:
                for n in file:
                        data = n.split(" ")
                        name=input('Enter the username of the person you would like to E-Transfer money to:')
                        if name == data[0]:
                                print('You are sending money from your chequing account')
                                money=input('How much money would you like to send to '+name+"?")
                                if money>data[2]:
                                        print('Insufficient funds')
                                        return
                                if money<data[2]:
                                        data[2]= int(data[2]) +money
                                        data[2]= int(data[2]) -money
                                        print('You have successfully transfered $' +money+ ' to' +name)
                                        y=False
                                else:
                                        print('That is not an account, which bank do toy bank at?')
                                
                        
                        elif name != data[0]:
                                print('That account does not exist')
                                return

start()
option()




















