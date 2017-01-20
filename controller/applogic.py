from model.cache import Cache
from views.interface import Interface

class applogic(object):

    def __init__(self, username):
        self.username = username
        self.user_skills = {}
        self.user_data = userdata()
        self.user_interface = Interface()

    def getskills_user (self, message = 'Please Enter your Username:'):
        '''remember to ask for uder i[ut message'''
        print(message)
        user_input = input()
        
        return user_input
    
    def addskills_user(self, skill):
        self.user_skills[skill].append(skill)

    def listskills(self, list_skills):
        data = self.user_data.getskills()

    def next_step(self, user_response):
        user_response = str(user_response)

        if user_response == 'a':
            #ask for input
            user_in = self.getskills_user("Please add your skill")
            self.user_skills[user_in] = user_in
        elif user_response == 'v':
            self.user_interface.viewskills(self.user_skills)
            pass
        elif user_response == 'd': #to be implemented
            pass

    def run(self):
        while(True):
            
            #display welcome message from views
            self.user_interface.initialize()
            #get input from user
            users_userinput = self.getskills_user()

            #get user response
            user_response = self.getskills_user("Please input a response")

            #call a fuction that decide what next
            self.next_step(user_response)

            #exit if e was pressed
            if user_response == 'e':
                print("Goodbye thank you")
                break
        return

         #given

 ##############################################
class userdata(object):
     data_DB = CACHE()
    def __init__(self, username = ''):

        self.username = username
        self.data = data_DB.get()

    def getskills(self):
        return data_DB

        

        
        
