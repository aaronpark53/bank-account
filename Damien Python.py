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
        username = input('Create a username: ')
        password = str(input('Password: Enter your 4 digit PIN number: '))
        if int(password) >=10000 or int(password) <=999:
                print("That's not 4, can you count?????")
                start()
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
        return
                                  

def login():
        global chequingBalance
        global savingsBalance
        global username
        global password
        global passwordLocation
        file = open('./passwords.txt').read()
        file=file.split("\n")
        login=True
        password=True
        x=3
        while login==True:
                while x>=0:
                        username=str(input('Enter your username: '))
                        userFound = False
                        for passwordLocation in range(len(file)):
                                data = file[passwordLocation].split(" ")
                                if data[0] == username:
                                        userFound = True
                                        while password==True and x>0:
                                                password=input('Enter your 4 digit PIN password: ')
                                                if password == data[1]:
                                                        print('Login Successful ')
                                                        password=False
                                                        login=False
                                                        chequingBalance= float(data[2])
                                                        savingsBalance= float(data[3])
                                                        username= data[0]
                                                        password= data[1]
                                                        return
                                                elif password != data[1]:
                                                        print('Incorrect Password ')
                                                        print('Re-enter your password')
                                                        password=True
                                                        x-=1
                        if userFound == False:
                                print('This username does not exist')
                                x-=1

def option():
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
                        printBalance()
                elif y==5:
                        print('Thank you for banking with the Bank')
                        break
                else:
                        print(y,'was not an option idiot head dumb face stupid head')

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
                        withdrawal=float(input('Input value of the withdrawal: '))
                        if withdrawal <= chequingBalance:
                                print('Current Chequing account balance: ', chequingBalance)
                                chequingBalance= chequingBalance - withdrawal
                                update()
                                print('New Chequing account balance: ', chequingBalance)
                                print('You have successfully withdrawn ', withdrawal, ' dollars')
                                return
                        else:
                                print('Insufficient Funds.')
                                return
                elif x==2:
                        withdrawal=int(input('Input value of the withdrawal: '))
                        if withdrawal <= savingsBalance:
                                print('Current Savings account balance: ', savingsBalance)
                                savingsBalance= savingsBalance - withdrawal
                                update()
                                print('New Savings account balance: ', savingsBalance)
                                print('Your deposit of: ', withdrawal, 'dollars was successful')
                                return
                        else:
                                print('Insufficient Funds.')
                                return
                elif x==3:
                        n=False
                        return
                else:
                        print('That is not an option. Try again. ')
                

def deposit():
        global chequingBalance
        global savingsBalance
        n=True
        while n==True:
                x=int(input('''Select account to deposit into:
1. Chequing
2. Savings
3. Go Back:
Enter(1/2/3):  '''))
                if x==1:
                        print('Current Chequing account balance: ', chequingBalance)
                        deposit=float(input('Input the value of your deposit: '))
                        chequingBalance=chequingBalance+deposit
                        update()
                        print('New Chequing account balance: ', chequingBalance)
                        print('Your deposit of ', deposit, 'dollars was successful.')
                        return
                elif x==2:
                        print('Current Savings account balance: ', savingsBalance)
                        deposit=float(input('Input the value of your deposit: '))
                        savingsBalance=savingsBalance+deposit
                        update()
                        print('New Savings account balance: ', savingsBalance)
                        return
                elif x==3:
                        n=False
                        return
                else:
                        print('That is not an option. Try again.')

def transferMoney():
        global chequingBalance
        global savingsBalance
        x=int(input('''Select option:
1. Chequing to Savings 
2. Savings to Chequing 
3. Go Back             
Enter(1/2/3):  '''))
        if x==1:
                print('Current Chequing account balance: ',chequingBalance)
                print('Current Savings account balance: ', savingsBalance)
                transferAmount=float(input('Input the value of the transfer: '))
                if transferAmount > chequingBalance:
                        print('Insufficient funds. ')
                        return
                else:
                        chequingBalance= chequingBalance-transferAmount
                        savingsBalance=savingsBalance+transferAmount
                        update()
                        print('You have successfully transferred ', transferAmount, 'from Chequings to Savings.')
                        print('''
New Chequing account balance: ''', chequingBalance)
                        print('New Savings account balance: ', savingsBalance)
                        return
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
                        return
        elif x==3:
                return
        else:
                print('That is not an option. ')
                
def printBalance():

        x=int(input('Select Account(1/2):  1. Chequing   2. Savings '))
        if x == 1:
                print(chequingBalance)
        elif x == 2:
                print(savingsBalance)


                

def update():
        global passwordLocation
        file = open('./passwords.txt').read()
        file=file.split("\n")[:-1]

        f = open('passwords.txt', 'w')

        for n in range(len(file)):
                if n == passwordLocation:
                        continue
                f.write(file[n] + '\n')
        
        f.write(username+ ' ' +password+ ' ' +str(chequingBalance) + ' ' + str(savingsBalance) + '\n')
        f.close()
        
        passwordLocation = len(file)-1
                





print('Welcome to the Bank. ')
start()
option()
