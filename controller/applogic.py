class applogic(object):
    def __init__(self, username, userdata, Interface):
        self.username = username
        self.user_skills = {}

        #objects to hold user data
        self.user_data = userdata
        #object to hol our use interface
        self.user_interface = Interface

    def get_user_input(self, message = ''):
        self.user_interface.AskForInput(message)
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
            user_in = self.get_user_input("Please add your skill")
            self.user_skills[user_in] = user_in
            self.user_interface.successMessage("Add Skill")
            self.pause_for_sometime()
        elif user_response == 'v':
            self.user_interface.viewskills(self.user_skills)
            pass
        elif user_response == 'd': #to be implemented
            pass

    def pause_for_sometime(self, time = 100):
        promt = -1
        while(promt == -1):
            promt = input("Press any key to continue: ")

    def run(self):
        #get input from user
        user_name = self.get_user_input('user name')

        #check for details in Db about this user
        greet_user = True

        while(True):
            #display welcome message from views
            self.user_interface.initialize(user_name, greet_user)

            #get user response
            user_response = self.get_user_input(" response")

            #exit if e was pressed
            if user_response == 'e':
                self.user_interface.goodbyeMessage(user_name)
                break

            #call a fuction that decide what next
            self.next_step(user_response)
            greet_user = False
        return

if __name__ == '__main__':
    #importing the required modules views and model is hard
    #so testing is to be done with main
    pass
