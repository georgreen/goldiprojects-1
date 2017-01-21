# this is the main app.
from controller.applogic import applogic
from model.cache import Cache
from views.interface import Interface

##############################################

if __name__  == '__main__':
    username = ''
    data = Cache() #Doin this cause an error 
    UI = Interface()
    newapp = applogic(username, data, UI)
    newapp.run()
