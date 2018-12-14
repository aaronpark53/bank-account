def createAccount():
        global username
        global password
        global initialDeposit
        username = str(input('Username: Create a username: '))
        password = int(input('Password: Enter your 4 digit PIN number: '))
        initialDeposit = float(input('Initial Deposit: Enter your initial deposit: '))

def login():
        username=str(input('Enter your email: '))
        password=int(input('Enter your 4 digit PIN password: '))

x=input('1. Create new account  2. Login')
if x == 1:
        createAccount()
elif x == 2:
        login()
