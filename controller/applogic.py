from model.cache import CACHE
from view.interface import Interface

class applogic(object):

    def __init__(self, username):
        self.username = username
        self.user_skills = {}
        self.user_data = userdata()
        self.user_interface = Interface()

    def getskills_user (self):
        '''remeber to ask for uder i[ut message'''
        print('Please Enter your Username: ')
        user_input = input()
        
        return user_input
    
    def addskills_user(self, skill):
        self.user_skills[skill] = skill

    def listskills(self, list_skills):
        data = self.user_data.getskills()
        
        

    def run(self):
        #display welcome message from views
        self.user_interface.initialize()

        #get input from user
        users_userinput = self.getskills_user()
            #get user name

         #display menu from views

         #

 ##############################################
from <path to this module> import cache
class userdata(object):
     data_DB = CACHE()
    def __init__(self, username = ''):

        self.username = username
        self.data = data_DB.get()

    def getskills(self):
        return data_DB

        

        
        
