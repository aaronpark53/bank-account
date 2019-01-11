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
