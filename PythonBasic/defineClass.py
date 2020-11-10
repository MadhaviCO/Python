class PartyAnimal:
	x = 0
	name = ""
	def __init__(self, nm):
		self.name = nm
		print(self.name, 'is constructed')
	def __del__(self):
		print(self.name, 'is destructed')

	def party(self):
		self.x = self.x + 1
		print(self.name, "partied", self.x, 'times')

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")
s.party()
s.party()
s.party()
s.party()
j.party()

print("Type", type(s))
print("Dir", dir(s))

s = 42
print('s contain', s)


