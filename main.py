import time as T
import random as r
import json as J 
class User: 
    
    def __init__(self, username, password, profile, posts= 0, badges=0, logged_in=False, moderator= False, owner= False ): 
       self.password= password 
       self.username= username
       self.posts = posts 
       self.profile= profile
       self.badges= badges
       self.logged_in= logged_in
       self.moderator= moderator 
       self.owner= owner 


    def owner_class(self): 
        if self.owner == False: 
            psswrd= input("what is the owner class password")
            if psswrd == "Peagravel3": 
                self.owner == True 
            else: 
                return "wrong, try again"
        else:
            return "you are already the owner"
        return "Owner class process successful. Welcome, owner."
    def assign_mod(self): 
        if self.owner== True: 
            name= input("what person would you like to make a mod")
            with open("users.json", "a") as a: 
                users= a. ## how to check for a class related input in a Json file and how to look for a variable of that user (username) 
            if name in users.username: 

    def prof(self):
        with open(self.profile, "w") as l: 
            content= l.readlines()
        return content 

    def post(self):
        txt= input("what would you like to post?")
        Post(txt,T.gmtime(),T.gmtime(), self.username, self.profile)
        return "post successful"
    
    def log_in(self, logged_in, entered_password, entered_username): 
        if logged_in == False: 
            entered_username= input("enter your username.")
            entered_password= input("enter a password")
            
    def comment(username, ): 
        pass
    def new_user_check(self, new_user): 
        with open("moderator_check.json", "a") as q: 
            if self.owner ==True: 
                new_user = input("which user would you like to approve/deny")
                if new_user in moderator_check.keys(): 
                    approval=input("do you approve this user?")
                    if approval == "yes" or "Yes": 
                        cont= False
                        while cont= False: 
                            with open("adjectives.txt", "r") as f:
                                readf= f.read()
                                adjective= list(map(str, readf.split()))
                            with open("nouns.txt","r") as g: 
                                readg= g.read()
                                noun= list(map(str,readg.split()))
                                new_name= (r.choice(adjective), r.choice(noun))  
                        with open("users.txt", "w") as l: 
                            user.keys = l.readlines()    
                        if new_name not in users.keys: 
                            cont= True
                        password = new_user[3]
                        with open(new_name, "x" ) as g : 
                            profile= g
                        usernew= User(new_name, password, profile)
                        
                        with open("users.json", "a") as h: 
                            h.writelines(usernew)
                            
                    else: 
                        pass 
                else: 
                    return "this user does not exist"
            else: 
                return "you do not have access to this function"
        return "user successfully created"

class Post(): 
    
    def __init__(self, words, time, date, username,profile ):
        pass
class Comment(): 

    def __init__(self, words, time, date, username):


        
def sign_up():
    name= input("what is your name")
    email= input("what is your email") 
    stnum= input("what is your st number?")
    password= input("what is your password? ")

    data_dict = {name:[email,stnum,password]}
    with open("moderator_check.json", "a") as f:
        f.writelines(data_dict)

    return data_dict