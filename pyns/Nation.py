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