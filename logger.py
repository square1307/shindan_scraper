#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
import codecs
import os

def timestamp():
	return math.floor(time.time())

class Logger:
	def __init__(self,strFilename = "", bPrintOnScreen = False, bOutToFile = True,strDirectory = "."):
		self.bPrintOnScreen = bPrintOnScreen
		self.bOutToFile = bOutToFile
		try:
			os.mkdir(strDirectory)
		except:
			pass
		if self.bOutToFile:
			if (strFilename == ""):
				self.strFilename = "{}.txt".format(str(int(timestamp())))
			else:
				self.strFilename = strFilename
			self.file = codecs.open(strDirectory + "/" + self.strFilename, "a", "utf-8")

	def output(self,input,bNewline = True):
		try:
			if (self.bOutToFile):
				if (bNewline == False):
					self.file.write(str(input))
				else:
					self.file.write("{}\n\n".format(str(input)))
			if self.bPrintOnScreen:
				print(str(input))
		except:
			print("ERROR DURING WRITING FILE")