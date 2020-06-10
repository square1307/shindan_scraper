#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logger
import scraper
import sys
import datetime
import time
import math

def timestamp():
	return math.floor(time.time())


id = 484265
url = "https://shindanmaker.com/a/{}"
strCharacterName = "."

if __name__ == "__main__":
	checking_scraper = scraper.Scraper()
	checking_scraper.changeURL(url.format(str(id)))
	checking_logger = logger.Logger(bPrintOnScreen = True, bOutToFile = True,strDirectory=datetime.datetime.now().strftime("%Y%m%d"))
	checking_logger.output("{}:{}".format(strID,checking_scraper.title()))
	checking_logger.output(datetime.datetime.now().strftime("%Y%m%d"))
	while strCharacterName.strip() != "":
		try:			
			strCharacterName = input("input:")
			if (strCharacterName.strip() == ""):
				break
			checking_logger.output("{}".format(strCharacterName))
			result = checking_scraper.IO(strCharacterName)
			checking_scraper.screenshot(datetime.datetime.now().strftime("%Y%m%d"),strCharacterName,strID)
			checking_scraper.previousPage()
			checking_scraper.min_window()
			checking_logger.output(result)
		except:
			pass
	checking_scraper.close()