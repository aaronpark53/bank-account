def newAccount(username,password,initialDeposit):
        import os
        file=open("./passwords.txt","a")
        file.write(username+' '+password+' '+initialDeposit+'\n')
        file.close()

global username
global password
global initialDeposit

username=input('::')
password=input(';;')
initialDeposit=input('$$')

newAccount(username,password,initialDeposit)






	
	
	
	
  









  














