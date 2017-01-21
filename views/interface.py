# Learncompanion project
#interface cli
class Interface(object):

    def __init__(self):
        pass

    def initialize(self, username = '', greet_user = False):
        if greet_user :
            print ("Hello " + username +" Welcome to Learn Companion")
        padding = 35
        self.print_tokken('.', padding)
        self.print_tokken(' ' * ((padding // 2) - 2 )+ "Menu" )
        self.print_tokken('.', padding)
        self.print_tokken('-', padding)
        self.print_tokken("Press -> 'a': Add Skill")
        self.print_tokken("Press -> 'v': View Skill")
        self.print_tokken("Press -> 'd': Delete Skill")
        self.print_tokken("Press -> 'e': Exit")
        self.print_tokken(".", padding)
        return

    def print_tokken(self, tokken = '.', span = 1, endx = '\n'):
        if endx == '\n':
            print(tokken * span)
        else:
            print(tokken * span, end = endx)

    def viewskills(self, skill_name, skill_list, label = True):
        if label:
            self.print_tokken('| SKILL' + ' ' * len(skill_name) +'| Sub Task' + ' ' * len(skill_list[0]) + '| Progress')
        self.print_tokken('   ' + skill_name + ' ' *len('SKILL'), 1, '')
        self.print_tokken('  ' + skill_list[0] + ' ' * len('Sub Task'), 1, '')
        self.print_tokken(' ' + str(skill_list[1]), 1, '')
        print()
        return

    def successMessage(self, taskdone = "Task"):
        print("Sucess: " + taskdone + " was completed succesfully")
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

    test.successMessage()
    test.ErrorMessage()
    test.AskForInput()
    test.goodbyeMessage()
    test.viewskills('Git', ['push', True])
