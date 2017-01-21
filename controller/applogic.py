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
        if skill in self.user_data:
            self.user_interface.ErrorMessage('Adding skill')
            self.user_interface.print_tokken('The skill ' + skill + ' Already exists!')
            return False
        else:
            self.user_skills[skill] = []#Buffer to hold new data
            self.user_data[skill] = [] #Add the input to DB
            return True

    def deleteskill_user(self, skill):
        if skill in self.user_data:
            self.user_data.pop(skill)
            return True
        else:
            self.user_interface.ErrorMessage('Delete skill')
            self.user_interface.print_tokken('The skill ' + skill + ' Does not EXIST in your skills')
            return False

    def listskills(self, list_skills):
        data = self.user_data.getskills()

    def next_step(self, user_response):
        user_response = str(user_response)

        if user_response == 'a':
            #ask for input
            user_in = self.get_user_input("Skill To BE ADDED")
            if self.addskills_user(user_in):
                self.user_interface.successMessage("Add Skill")
            else:
                pass
            self.pause_for_sometime()
        elif user_response == 'v':
            show_label = True
            for skill in self.user_data:
                self.user_interface.viewskills(skill, self.user_data[skill], show_label)
                show_label = False
            self.pause_for_sometime()
        elif user_response == 'd':
            user_in = self.get_user_input("Skill TO BE DELETED")
            if self.deleteskill_user(user_in):
                self.user_interface.successMessage("Delete Skill")
            else:
                pass
            self.pause_for_sometime()

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
                self.user_data.save() #Store all the changes [Persistent data]
                break

            #call a fuction that decide what next
            self.next_step(user_response)
            greet_user = False
        return

if __name__ == '__main__':
    #importing the required modules views and model is hard
    #so testing is to be done with main
    pass
