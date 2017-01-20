# Learncompanion project
#interface cli
class Interface(object):
	"""docstring for interface"""
	def __init__(self, command='x',status=True):
		self.command = command
		self.status = status
	def initialize(self):
		if (self.command =='x'):
			print ("Welcome to Learn Companion")
			print ("--------------------------")
			print ("'a': Add Skill")
			print ("'v': View Skill")
			print ("'d': Delete Skill")
			print ("'e': Exit")
			self.command = input("Enter Command: ")
		elif self.command=='a':
			addskill(self, skillname,skilldescription)
		elif self.command=='v':
			pass
		elif self.command=='e':
			pass
		else:
			print ("Invalid command: ")
			print ("Enter command:")

	def addskill(self, skillname,skilldescription=""):
		print ("skill called")

	def viewskills(skill_list):
		pass
	def exitapp():
		pass

interface = Interface()
interface.initialize()