class colored:
	def __init__(self, text, color='\033[1000m',  highlight='\033[1000m',  effect='\033[1000m'):
		self.text = text
		none = '\033[1000m'
		#---- color ----
		Lred = '\033[91m'
		red = '\033[31m'
		Lblue = '\033[94m'
		blue = '\033[34m'
		Lgreen = '\033[92m'
		green = '\033[32m'
		yellow = '\033[93m'
		cyan = '\033[96m'
		Lcyan = '\033[36m'
		pink = '\033[95m'
		gray = '\033[90m'
		Lgray = '\033[37m'
		black = '\033[30m'
		purple = '\033[35m'
		orange = '\033[33m' 
		if color == "red":
			self.color = red
		elif color == "blue":
			self.color = blue	
		elif color == "green":
			self.color = green
		elif color == "yellow":
			self.color = yellow
		elif color == "pink":
			self.color = pink
		elif color == "gray":
			self.color = gray
		elif color == "purple":
			self.color = purple
		elif color == "cyan":
			self.color = cyan	
		elif color == "black":
			self.color = black	
		elif color == "orange":
			self.color = orange	
		elif color == "Lred":
			self.color = Lred	
		elif color == "Lcyan":
			self.color = Lcyan		
		elif color == "Lgreen":
			self.color = Lgreen
		elif color == "Lblue":
			self.color = Lblue	
		elif color == "Lgray":
			self.color = Lgray
		else:
			self.color = none
		#---- highlight ----	
		on_Lred = '\033[101m'
		on_Lblue = '\033[104m'
		on_Lgreen = '\033[102m'
		on_black = '\033[40m'
		on_red = '\033[41m'
		on_blue = '\033[44m'
		on_green = '\033[42m'
		on_yellow = '\033[103m'
		on_Lcyan = '\033[106m'
		on_cyan = '\033[46m'
		on_pink = '\033[105m'
		on_Lgray = '\033[47m'
		on_gray = '\033[100m'
		on_white = '\033[107m'
		on_orange = '\033[43m'
		on_purple = '\033[45m'
		if highlight == "on_red":
			self.highlight = on_red
		elif highlight == "on_blue":
			self.highlight = on_blue	
		elif highlight == "on_green":
			self.highlight = on_green
		elif highlight == "on_yellow":
			self.highlight = on_yellow
		elif highlight == "on_pink":
			self.highlight = on_pink
		elif highlight == "on_gray":
			self.highlight = on_gray
		elif highlight == "on_white":
			self.highlight = on_white			
		elif highlight == "on_Lblue":
			self.highlight = on_Lblue	
		elif highlight == "on_Lgreen":
			self.highlight = on_Lgreen
		elif highlight == "on_Lred":
			self.highlight = on_Lred
		elif highlight == "on_black":
			self.highlight = on_black
		elif highlight == "on_Lgray":
			self.highlight = on_Lgray
		elif highlight == "on_orange":
			self.highlight = on_orange
		elif highlight == "on_purple":
			self.highlight = on_purple
		elif highlight == "on_Lcyan":
			self.highlight = on_Lcyan
		elif highlight == "on_cyan":
			self.highlight = on_cyan
		else:
			self.highlight = none
		#---- effect ----
		bold = '\033[1m'
		underline = '\033[4m'
		if effect == "bold":
			self.effect = bold
		elif effect == "underline":
			self.effect = underline
		else:
			self.effect = none
	
	def __repr__(self):
		return self.color + self.highlight + self.effect + self.text + '\033[0m'