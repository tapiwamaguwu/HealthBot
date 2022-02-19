from ast import Dict
from datetime import datetime
from typing import Any
# from typing_extensions import Self
from utils.auth import Auth
from peewee import *
from utils.db import getDBConnection

# initialising the authentication service
auth = Auth()
db = getDBConnection()


class User(Model):
    username = CharField()
    password = CharField()
    email = CharField(unique=True)
    join_date = DateTimeField()

    class Meta:
        database = db
        db_table='User'

    # # creates and saves object to database, returns boolean (True is user is created in database) plus the User object or a dictionary with the error message
    # def __init__(self, name: str, email: str, password: str):
    #     try:
    #         with db.atomic():
    #             self.username=name
    #             self.password=auth.get_password_hash(password), 
    #             self.email=email,
    #             self.join_date=datetime.now()
    #             self.save()
    #             self.
    #             return True,self
                
                 

    #     except IntegrityError as e:
    #         print("User(): ",e)
    #         return {"error":"An account with this email address already exists"}         

def create_tables():
    with db:
        db.create_tables([User])


# creates and saves object to database, returns boolean (True is user is created in database) plus the User object or a dictionary with the error message
def create_user(name: str, email: str, password: str):
    success=False
    user=None
    try:
        with db.atomic():
            user = User.create(
            username=name,
            password=auth.get_password_hash(password), 
            email=email,
            join_date=datetime.now()
            )
            success=True
            
            
    except IntegrityError as e:
        print("User(): ",e)
        success=False
        user = {"error":"An account with this email address already exists"}         

    return success,user    


# retrieves user 
def get_user(email: str):
    user= None
    success=False
    try:
        user = User.get(User.email==email)
        success=True
    except DoesNotExist as e: 
        print("get_user(): ",e)  
        success=False 
    return success,user

def authenticate(email:str,password: str)->bool:
    authenticated=False
    success,user=get_user(email)
    if(success):
        authenticated=auth.verify_password(password,user.password)
        
    return authenticated   

# creates Model definitions
create_tables()