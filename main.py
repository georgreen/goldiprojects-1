# this is the main app.
from controller.applogic import applogic
from model.cache import Cache
from views.interface import Interface

##############################################
class userdata(object):
   def __init__(self, username = ''):
       self.username = username

   def getskills(self):
       return

if __name__  == '__main__':
    username = ''
    data = userdata()
    UI = Interface()
    newapp = applogic(username, data, UI)
    newapp.run()
