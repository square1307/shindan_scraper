#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
import os

def timestamp():
	return math.floor(time.time())

class Logger:
	def __init__(self,strFilename = "", bPrintOnScreen = False, bOutToFile = True):
		self.bPrintOnScreen = bPrintOnScreen
		self.bOutToFile = bOutToFile

		if self.bOutToFile:
			if (strFilename == ""):
				self.strFilename = "{}.txt".format(str(timestamp()))
			else:
				self.strFilename = strFilename
			strDir = os.path.join(os.path.dirname(__file__), 'logs/'+self.strFilename)
			self.file = open(strDir, 'a')

	def output(self,input,bNewline = True):
		try:
			if (self.bOutToFile):
				if (bNewline == False):
					self.file.write(str(input))
				else:
					self.file.write("{}\n".format(str(input)))
			if self.bPrintOnScreen:
				print(str(input))
		except:
			print("ERROR DURING WRITING FILE")
