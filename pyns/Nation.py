"""This will be the main file for the Nations API Wrapper"""
class Freedom:
	def __init__(self):
		self.civilrights = ""
		self.economy = ""
		self.politicalfreedom = ""

class FreedomScores:
	def __init__(self):
		self.civilrights = 0
		self.economy = 0
		self.politicalfreedom = 0

class Deaths:
	def __init__(self):
		"""The respective percentages of the causes of death"""
		self.wilderness = 0
		self.exposure = 0
		self.capital = 0
		self.murder = 0
		sefl.heart = 0
		self.age = 0

class Nation:
	def __init__(self):
		self.name = ""
		self.fullname = ""
		self.type = ""
		self.motto = ""
		self.category = ""
		self.wa = False
		self.endorsements = 0
		self.gavote	= ""
		self.scvote = ""
		self.freedom = Freedom()
		self.region = ""
		self.population = 0
		self.tax = 0
		self.animal = ""
		self.animaltrait = ""
		self.currency = ""
		self.flag = "" # A link
		self.majorindustry = ""
		self.crime = ""
		self.sensibilities = ""
		self.govtpriority = ""
		self.govt = ""
		self.govtdesc = ""
		self.industrydesc = ""
		self.notable = ""
		self.admirable = ""
		self.founded = 0
		self.firstlogin = 0
		self.lastlogin = 0
		self.lastactivity = 0
		self.influence = ""
		self.freedomscores = FreedomScores()
		self.publicsector = 0
		self.deaths = Deaths()
		self.leader = ""
		self.capital = ""
		self.religion = ""
		self.customleader = ""
		self.customcapital = ""
		self.customreligion = ""
		self.rcensus = 0
		self.wcensus = 0
		self.censusscore = 0
		self.legislation = False ### To Do
		self.happenings =  False ### To Do
		self.censusscoren = False ### To Do
	
	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def setAttribute(self, attribute, value):
		if attribute == "name":
			self.name = value
		elif attribute == "fullname":
			self.fullname = value
		elif attribute == "type":
			self.type = value
		elif attribute == "motto":
			self.motto = value
		elif attribute == "category":
			self.category = value
		elif attribute == "wa":
		self.wa = value
		elif attribute == "endorsements":
			self.endorsements = value
		elif attribute == "gavote	=":
			self.gavote	= = value
		elif attribute == "scvote":
			self.scvote = value
		elif attribute == "region":
			self.region = value
		elif attribute == "population":
			self.population = value
		elif attribute == "tax":
			self.tax = value
		elif attribute == "animal":
			self.animal = value
		elif attribute == "animaltrait":
			self.animaltrait = value
		elif attribute == "currency":
			self.currency = value
		elif attribute == "flag":
			self.flag = value
		elif attribute == "majorindustry":
			self.majorindustry = value
		elif attribute == "crime":
			self.crime = value
		elif attribute == "sensibilities":
			self.sensibilities = value
		elif attribute == "govtpriority":
			self.govtpriority = value
		elif attribute == "govt":
			self.govt = value
		elif attribute == "govtdesc":
			self.govtdesc = value
		elif attribute == "industrydesc":
			self.industrydesc = value
		elif attribute == "notable":
			self.notable = value
		elif attribute == "admirable":
			self.admirable = value
		elif attribute == "founded":
			self.founded = value
		elif attribute == "firstlogin":
			self.firstlogin = value
		elif attribute == "lastlogin":
			self.lastlogin = value
		elif attribute == "lastactivity":
			self.lastactivity = value
		elif attribute == "influence":
			self.influence = value
		elif attribute == "publicsector":
			self.publicsector = value
		elif attribute == "leader":
			self.leader = value
		elif attribute == "capital":
			self.capital = value
		elif attribute == "religion":
			self.religion = value
		elif attribute == "customleader":
			self.customleader = value
		elif attribute == "customcapital":
			self.customcapital = value
		elif attribute == "customreligion":
			self.customreligion = value
		elif attribute == "rcensus":
			self.rcensus = value
		elif attribute == "wcensus":
			self.wcensus = value
		elif attribute == "censusscore":
			self.censusscore = value