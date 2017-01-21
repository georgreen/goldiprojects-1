import json;

class Cache(dict):
	
	def __init__(self):
		target = open('model/cache.json', 'r')
		super(Cache, self).__init__(json.loads(str(target.read())))
		target.close()
		
	def get(self, outcome = None):
		if outcome is not None:
			return self.get(outcome, None)
		else:
			return self

	def save(self):
		target = open('model/cache.json', 'w')
		target.write(json.dumps(self))
		target.close()

		
