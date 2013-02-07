import xml.etree.ElementTree as ET
from mechanize import Browser
from bs4 import BeautifulSoup

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

class Government:
	def __init__(self):
		self.environment = 0
		self.socialequality = 0
		self.education = 0
		self.lawandorder = 0
		self.administration = 0
		self.welfare = 0
		self.spirituality = 0
		self.defence = 0
		self.publictransport = 0
		self.healthcare = 0
		self.commerce = 0

class Deaths:
	def __init__(self):
		"""The respective percentages of the causes of death"""
		self.wilderness = 0
		self.exposure = 0
		self.capital = 0
		self.murder = 0
		self.heart = 0
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
		self.govt = Government()
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
		"""Get nation name, can alternatively be done with nation.name"""
		return self.name

	def setName(self, name):
		"""Set nation name"""
		self.name = name

	def setAttribute(self, attribute, value):
		"""Given an attribute name, and a value, this function updates the nation instance's attribute."""
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
			self.endorsements = int(value)
		elif attribute == "gavote":
			self.gavote	== value
		elif attribute == "scvote":
			self.scvote = value
		elif attribute == "region":
			self.region = value
		elif attribute == "population":
			self.population = int(value)
		elif attribute == "tax":
			self.tax = int(value)
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
			self.founded = int(value)
		elif attribute == "firstlogin":
			self.firstlogin = int(value)
		elif attribute == "lastlogin":
			self.lastlogin = int(value)
		elif attribute == "lastactivity":
			self.lastactivity = int(value)
		elif attribute == "influence":
			self.influence = value
		elif attribute == "publicsector":
			self.publicsector = int(value)
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
			self.rcensus = int(value)
		elif attribute == "wcensus":
			self.wcensus = int(value)
		elif attribute == "censusscore":
			self.censusscore = int(value)
		elif attribute == "govt":
			assert type(value) == type(Government()), self.govt = value
		elif attribute == "freedom":
			assert type(value) == type(Freedom()), self.freedom = value
		elif attribute == "freedomscores":
			assert type(value) == type(FreedomScores()), self.freedomscores = value
		elif attribute == "deaths":
			assert type(value) == type(Deaths()), self.deaths = value
		
	def readAttribute(self, attribute, nation, autoset = True, debug = False):
		"""This function takes an attribute and reads it from a link for a particular nation. Auto updating of the nation's value defaults to True, debugging defaults to False.
		More complicated data to read, such as freedom scores, government budget breakdown, how the nation's freedom is and the breakdown of death rates have yet to be finished.""" 
		baseUrl = "http://www.nationstates.net/cgi-bin/api.cgi?nation="
		readUrl = baseUrl + "%s&q=%s" % (nation, attribute)
		### Now do something to get the data
		### ...
		### xmlData is the xml data returned by the Nationstates API
		br = Browser()
		br.open(readUrl)
		xmlData = br.response().read()
		root = ET.fromstring(xmlData)
		complexAttributes = ["govt", "freedom", "freedomscores", "deaths"]

		if attribute not in complexAttributes:
			returnVal = root.find((attribute.upper())).text
		else:
			if attribute == "govt":
				g = Government()
				g.environment = root.find("ENVIRONMENT").text
				g.socialequality = root.find("SOCIALEQUALITY").text
				g.education = root.find("EDUCATION").text
				g.lawandorder = root.find("LAWANDORDER").text
				g.administration = root.find("ADMINISTRATION").text
				g.welfare = root.find("WELFARE").text
				g.spirituality = root.find("SPIRITUALITY").text
				g.defence = root.find("DEFENCE").text
				g.publictransport = root.find("PUBLICTRANSPORT").text
				g.healthcare = root.find("HEALTHCARE").text
				g.commerce = root.find("COMMERCE").text
				returnVal = g
			elif attribute == "freedom":
				fr = Freedom()
				fr.civilrights = root.find("CIVILRIGHTS").text
				fr.economy = root.find("ECONOMY").text
				fr.politicalfreedom = root.find("POLITICALFREEDOM").text
				returnVal = fr
			elif attribute == "freedomscores":
				fr = FreedomScores()
				fr.civilrights = root.find("CIVILRIGHTS").text
				fr.economy = root.find("ECONOMY").text
				fr.politicalfreedom = root.find("POLITICALFREEDOM").text
				returnVal = fr
			elif attribute == "deaths"
				d = Deaths()
				d.wilderness = root.find("Lost in Wilderness").text
				d.exposure = root.find("Exposure").text
				d.capital = root.find("Capital Punishment").text
				d.murder = root.find("Murder").text
				d.heart = root.find("Heart Disease").text
				d.age = root.find("Old Age").text
				returnVal = d

		if autoset == True:
			self.setAttribute(attribute, returnVal)
			if debug == True:
				print "%s set" % attribute
		else:
			pass
		return returnVal
			
