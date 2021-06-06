import os, random, re
def check(nm):
    try:
        fread=open(nm)
    except IOError:
        fcreate=open(nm,"x")
        fcreate.close()

def checkuser(nm):
    try:
        fread=open(nm)
        return 1
    except IOError:
        print("Username not found!!")
        input()
        return 0


filename="project2userdata.txt"
check(filename)


def encryption(message):
    a=[]
    a.append(str(random.randint(0,9)))
    a.append(str(random.randint(0,9)))
    a.append(str(random.randint(0,9)))
    a.append(str(random.randint(0,9)))
    key=''.join(a)
    key=int(key)
    a.clear()
    for i in message:
        a.append(str(ord(i)^key))

    return a, key


def decryption(message,key):
    message=re.split('(\d+)',message)
    temp=''
    for i in message:
        if i.isdigit():
            temp+=chr(int(i)^int(key))

    return temp
      

def openapp(usr):
    userfile=usr+".txt"
    check(userfile)
    if os.path.getsize(userfile)==0:
        print("Application:No messages yet")
    else:
        fread=open(userfile,"r")
        for i in fread.readlines():
            key=i[:4]
            message=i[5:]
            message=message.strip("\n")
            print(decryption(message,key))


def sendmessage(usr,to_person):
        message=input(f"message to {to_person}: ")
        message=str(usr)+":"+message
        message, key=encryption(message)
        to_person+=".txt"
        fwrite_to_person=open(to_person,"a+")
        fwrite_to_person.write(f"{key}z")
        for i in message:
            fwrite_to_person.write(f"{i}f")
        fwrite_to_person.write("\n")
        fwrite_to_person.close()
        fwrite_to_self=open(usr+".txt","a+")
        fwrite_to_self.write(f"{key}z")
        for i in message:
            fwrite_to_self.write(f"{i}f")
        fwrite_to_self.write("\n")
        fwrite_to_self.close()


def sender(ch, to_person, username):
    if ch==1:
        to_person+=".txt"
        if checkuser(to_person) == 1:
            to_person=to_person.strip(".txt")
            sendmessage(username, to_person)
            ch=int(input("want to send messages:(1-yes/2-yes but other user/0-no): "))
            return ch

    if ch==2:
        to_person=''
        to_person=input("Recipent username: ")
        to_person+=".txt"
        if checkuser(to_person) == 1:
            print("User ID found")
            to_person=to_person.strip(".txt")
            sendmessage(username, to_person)
            ch=int(input("want to send messages:(1-yes/2-yes but other user/0-no): "))
            return ch

    if ch==0:
        print("Thankyou")

    
username=input('User ID: ')
password=input('Password: ')
fread=open(filename,"r")
for x in fread.readlines():
    data=list(x.split())
    if username==data[0] and password==data[1]:
        openapp(username)
        choice=int(input("want to send messages:(1-yes/0-no): "))
        if choice==1:
            to_person=input("Recipent username: ")

        while choice == 1 or choice == 2:
            if choice==1:
                choice=sender(choice, to_person, username)
            elif choice==2:
                choice=sender(choice," ", username)


        input()
