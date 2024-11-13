import time as T
import random as r
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


    def prof(self, username, posts):
        pass


    def post(self,username,  ):
        pass
    
    def log_in(self, logged_in, entered_password, entered_username): 
        pass
    def comment(username, ): 
        pass
    def new_user_check(self, new_user): 
        if self.owner ==True: 
            new_user = input("which user would you like to approve/deny")
            if new_user in moderator_check: 
                approval=input("do you approve this user?")
                if approval == "yes" or "Yes": 
                    new_name= r.adjective,r.noun
                    password = new_user[3]
                    profile= ##create profile with username as title
                    User(new_name, password, profile)
                else: 
                    pass 
        else: 
            print("you do not have access to this function")

class Post(User): 
    
    def __init__(self, words, time, date, username,profile ):
        super().__init__(username, profile)
        pass
class Comment(Post): 

    def __init__(self, words, time, date, username):

        super().__init__(words, time, date, username)
        
def sign_up():
    name= input("what is your name")
    email= input("what is your email") 
    stnum= input("what is your st number?")
    password= input("what is your password? ")

    data_dict = {name:[email,stnum,password]}
    with open("moderator_check", "a") as f:
        f.writelines(data_dict)
    return data_dict
    ##upload to moderator check