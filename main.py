import datetime 
import random as r
import json as J 
import pickle 
date= datetime.date.today()

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

    def get_usename(self): 
        return self.username

    def owner_class(self): 
        if self.owner == False and self.logged_in == True: 
            psswrd= input("what is the owner class password")
            if psswrd == "Peagravel3": 
                self.owner == True 
            else: 
                return "wrong, try again"
        else:
            return "you are already the owner"
        return "Owner class process successful. Welcome, owner."
    def assign_mod(self): 
        if self.owner== True and self.logged_in == True: 
            name= input("what person would you like to make a mod")
            with open('userfile.pkl', "ab") as a: 
                for users in a: 
                    usernamel= users.get_username()
            if name in usernamel and name == User.username:
                User.moderator= True
        else: 
            print("no can do partner")
        return self.moderator
             

    def prof(self):
        with open(self.profile, "r") as l: 
            content= l.readlines()
        return content 

    def post(self):
        if self.logged_in== True: 

            txt= input("what would you like to post?")
            newpost= Post(txt,date, self.username, self.profile)
            with open('post.pkl', 'ab') as g: 
                pickle.dump(newpost, g)
            with open(self.profile, "w") as f: 
                f.writelines(txt, f)
        else: 
            return "you are not logged in"
        return "post successful"
    
    def log_in(self): 
        if self.logged_in == False: 
            entered_username= input("enter your username.")
            entered_password= input("enter a password")
            if entered_username == self.username and entered_password == self.password: 
                self.logged_in == True 
            else: 
                return "incorrect username or password, please try again."
        else: 
            return "you are already logged in."
        return self.logged_in
            
    def comment(self):
        post_user= input("who made the post?")
        post_date= input("what date was the post made?")
        comment= input("what would you like to comment?")
        new_comment= Comment(comment,date, self.username)
        new_comment.comment()## not part of project 


        pass
    def new_user_check(self, new_user): 
        with open("moderator_check.json", "a") as q: 
            moderator_check = J.load(q)
            if self.owner ==True: 
                new_user = input("which user would you like to approve/deny")
                if new_user in moderator_check.keys(): 
                    approval=input("do you approve this user?")
                    if approval == "yes" or "Yes": 
                        cont= False
                        while cont == False: 
                            with open("adjectives.txt", "r") as f:
                                readf= f.read()
                                adjective= list(map(str, readf.split()))
                            with open("nouns.txt","r") as g: 
                                readg= g.read()
                                noun= list(map(str,readg.split()))
                                new_name= (r.choice(adjective), r.choice(noun))  
                        with open("users.txt", "r") as l: 
                            user_keys = l.readlines()    
                        if new_name not in user_keys: 
                            cont= True
                        password = new_user[3]
                        with open(new_name, "x" ) as g : 
                            profile= g
                        usernew= User(new_name, password, profile)
                        
                        with open('userfile.pkl', 'ab') as h: 
                            pickle.dump(usernew, h)
                            
                    else: 
                        pass 
                else: 
            
                    return "this user does not exist"
            else: 
                return "you do not have access to this function"
        return "user successfully created"

class Post(): 
    
    def __init__(self, words, time, username, likes):
        self.words= words 
        self.time= datetime.fromtimestamp(time.time())
        self.username= username 
        self.likes = likes 
class Comment(): 

    def __init__(self, words, time, username ):
        self.words= words 
        self.time= time 
        self.username= username
        pass #Not doing comments, way too hard to format right. 


        
def sign_up():
    name= input("what is your name")
    email= input("what is your email") 
    stnum= input("what is your st number?")
    password= input("what is your password? ")

    data_dict = {name:[password, stnum, email]}
    with open("moderator_check.json", "a") as f:
        J.dump(data_dict, f)
        

    return data_dict
    
Ownerprof= open("ownerprof.txt", "r")

with open('userfile.pkl', 'ab') as a:
    LJ= User("Liam(owner)", "Peagravel3", "ownerprof.txt" )
    pickle.dump(LJ, a)
User.log_in(LJ)
User.owner_class(LJ)