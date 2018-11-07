
import fbchat 
from getpass import getpass 
msg=fbchat.Message(text='HAPPY DEEPAVALI')
username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
users = client.fetchAllUsers() 
for i in users:   
    sent = client.send(msg, thread_id=i.uid) 
    
