# Abdul-Mohiz

name=input("Name : ")

username=input("User name : ")

password=input("Password : ")

data=f'\n\nName="{name}"    User name="{username}"    Password="{password}" '

f=open("passwords.txt","a")
f.write(data)
f.close()

print("*****saved seceusful*****")
print('your password saved in c:/passowrds.txt file ')
