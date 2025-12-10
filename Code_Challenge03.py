from getpass import getpass
# Username & Password
username = "Maningas"
password = "Hanniel"

# Login Process
yourusername = input("HI what is your username --> ")
yourpassword = getpass("Type your password please --> ")

#Checking
if yourusername == username and yourpassword == password:
	print('Access Granted')
else:
	print('Access Denied')
