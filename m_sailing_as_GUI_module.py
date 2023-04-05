import math as m

#must be entered with decimal degrees converted already
class M_Sailing:
	def __init__(self, lat1, ns1, lon1, ew1, lat2, ns2, lon2, ew2):
		self.lat1 = lat1
		self.ns1 = ns1
		self.lon1 = lon1
		self.ew1 = ew1
		self.lat2 = lat2
		self.ns2 = ns2
		self.lon2 = lon2
		self.ew2 = ew2

	# Find meridional parts
	def mp(self):
		#tsart of math
		lats = [self.lat1, self.lat2]
		merds = [] #list of the two meridional parts filled by for loop
		for lat in lats:
			e = 0.08248339904
			degree2 = 45 + (lat/2)
			radian = lat * 2 * m.pi/360
			radian2 = degree2 * 2 * m.pi/360
			result1 = m.tan(radian2)
			result2 = (1 + e *m.sin(radian))/(1-e*m.sin(radian))
			result2 = m.pow(result2,(e/2))
			result1 = m.log((result1/result2))*3437.746771
			merds.append(result1)
		if self.ns1 == self.ns2:
			dmp = abs(merds[0]-merds[1])
		elif self.ns1 != self.ns2:
			dmp = merds[0]+merds[1]
		return dmp

	#Dlong
	def dlong(self):
		if self.ew1 == self.ew2:
			dlon = abs(self.lon1 - self.lon2)*60 
		elif self.ew1 != self.ew2:
			if (self.lon1 + self.lon2) > 180:
				dlon = (360 - (self.lon1 + self.lon2))*60	
			elif (self.lon1 + self.lon2) <= 180:
				dlon = (self.lon1 + self.lon2)*60
		return dlon

	#dlat
	def dlat(self):
		if self.ns1 == self.ns2:
			dla = abs(self.lat1 - self.lat2)*60
		elif self.ns1 != self.ns2:
			dla = (self.lat1 + self.lat2)*60 
		return dla

	#Find Course
	def course(self):
		director = self.direction()
		dmp = self.mp()
		cse = m.degrees(m.atan(self.dlong()/dmp))
		if director == ['n','w']:
			cse_true = 360 - cse
			cse_true = round(cse_true,1)
		elif director == ['s','w']:
			cse_true = 180 + cse
			cse_true = round(cse_true,1)
		elif director == ['n', 'e']:
			cse_true = cse 
			cse_true = round(cse_true,1)
		elif director == ['s','e']:
			cse_true = 180 - cse
			cse_true = round(cse_true,1)
		return cse_true

	#Unadjusted course used for distance measurement	
	def c_uncorrected(self):
		dmp = self.mp()
		c_uncorr = m.degrees(m.atan(self.dlong()/dmp))
		return c_uncorr

	#Find departure
	def departure(self):
		rads = m.radians(self.c_uncorrected())
		d = self.dlat()/m.cos(rads)
		d = round(d,1)
		return d


	#Determine direction of travel
	def direction(self):
		director = []
		#North latitude start
		if self.ns1 == 'n':
			if self.ns1 == self.ns2:
				if self.lat2 > self.lat1:
					director.append("n")
				elif self.lat2 < self.lat1:
					director.append("s")
			elif self.ns1 != self.ns2:
				director.append("s")
	

		#South Latitude start
		if self.ns1 == 's':
			if self.ns1 == self.ns2:
				if self.lat2 > self.lat1:
					director.append("s")
				elif self.lat2 < self.lat1:
					director.append('n')
			elif self.ns1 != self.ns2:
				director.append('n')
	

		#West longitude start
		if self.ew1 == 'w':
			if self.ew1 == self.ew2:
				if self.lon2 > self.lon1:
					director.append('w')
				elif self.lon2 < self.lon1:
					director.append('e')
			elif self.ew1 != self.ew2:
				if (self.lon1 + self.lon2) >= 180.1:
					director.append('w')
				elif (self.lon1 + self.lon2) <= 180:
					director.append('e')


		#East longitude start
		if self.ew1 == 'e':
			if self.ew1 == self.ew2:
				if self.lon2 > self.lon1:
					director.append('e')
				elif self.lon2 < self.lon1:
					director.append('w')
			elif self.ew1 != self.ew2:
				if (self.lon1 + self.lon2) >= 180.1:
					director.append('e')
				elif (self.lon1 + self.lon2) <= 180:
					director.append('w')
		return director

	#Parallel sailing for when course in straight E/W
	def parallel(self):
		latitude = m.radians(self.lat1)
		dep = self.dlong() * m.cos(latitude)
		dep = round(dep,1)
		return dep

	#For presenting the solution in the GUI
	def m_run(self):
		if self.direction() == ['w']:
			distance = self.parallel()
			heading = 270

		elif self.direction() == ['e']:
			distance = self.parallel()
			heading = 90

		elif self.direction() == ['n']:
			distance = self.dlat()
			distance = round(distance,1)
			heading = 000

		elif self.direction() == ['s']:
			distance = self.dlat()
			distance = round(distance,1)
			heading = 180

		else:
			distance = self.departure()
			heading = self.course()

		answer = f"{distance} NM at {heading}° true"
		return answer


#---------------------TESTS-------------------------------
#ans = M_Sailing(25, "s", 172, "w", 15, "s", 170, "w")
#ans = M_Sailing(42.75, "n", 38.33, "w", 27.5, "n", 56.25, "w")
#print(f"The course is {ans.course()} degrees, and the distance is {ans.departure()} NM.")
#print(ans.m_run())