# Learncompanion project
#interface cli
class Interface(object):

    def __init__(self):
        pass

    def initialize(self, username = '', greet_user = False):
        if greet_user :
            print ("Hello " + username +" Welcome to Learn Companion")
        print("-----------------------------")
        print("          MENU               ")
        print(".............................")
        print("-----------------------------")
        print ("Press -> 'a': Add Skill")
        print ("Press -> 'v': View Skill")
        print ("Press -> 'd': Delete Skill")
        print ("Press -> 'e': Exit")
        print("...........................")
        return
    
    def viewskills(self, skill_dict):
        return

    def successMessage(self, taskdone = "Task"):
        print("Sucess the " + taskdone + " was completed succesfully")
        return

    def ErrorMessage(self, taskFailed = "task"):
        print("We aplogize there was an erro when doing " + taskFailed)
        return
    def AskForInput(self, inputMessage = 'data'):
        print("Please Enter your " + inputMessage)
        return
    def goodbyeMessage(self, user_name = "user"):
        print("Goodbye " + user_name +" thank you for using our App.")
        return


if __name__ == '__main__':
    test = Interface()
    test.initialize()
    test.viewskills({})
    test.successMessage()
    test.ErrorMessage()
    test.AskForInput()
    test.goodbyeMessage()
