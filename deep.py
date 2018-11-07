
import fbchat 
from getpass import getpass 

username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
users = client.fetchAllUsers() 
msg=fbchat.Message(text=input("Enter The Message You Want To Send : \t"))
for i in users:
    ss=  str("Uname : "+i.name +"\t ID :"+i.uid+'\n')
    print ("Uname : "+i.name +" \tID :"+i.uid)
    c=int(input("Send Msg To This User : y(1)/n(0)"))  
    f = open("log.txt","a")
    if(c==1) :
	    f.write(ss+'\n'+msg+'\n\n')
	    sent = client.send(msg, thread_id=i.uid) 
    
