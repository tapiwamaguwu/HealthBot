# For console
from chatbot import chat
from models.user import *

logged_in=False
option_selected=""
print("\n\n\nWelcome To HealthBot. \n")
while True:
  if(logged_in):
    message=input("You: ")
    res = chat(message)
    print("HealthBot: ",res)
  else:
    if(option_selected==""):
      option_selected=input("You are not logged in.\nOptions:\n1. Login\n2. Register\n\nType option number: ")
    elif(option_selected=="1"): 
      credentials = input("Enter your email address and password (separated by a space): ").split()
      logged_in=authenticate(credentials[0],credentials[1])
      if(logged_in):
        print("Login Successful\n\n\nYou can now chat to HealthBot. Start typing below...\n")
      else:
        print("Either the password or email are incorrect. Login unsuccesful")
        option_selected=""
    elif(option_selected=="2"):
      user_details =input("Enter your username, email address and password (separated by space): ").split()
      success,user=create_user(user_details[0],user_details[1],user_details[2])
      if(success):
        print("Your profile has been successfully created.\n\n\n You can now chat to HealthBot. Start typing below...\n ")
        option_selected=""
        logged_in=True
      else:
        print("Failed to create profile: ",user['error'])      
        option_selected=""

