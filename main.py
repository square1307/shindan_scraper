#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logger
import scraper

id = -1
url = "https://shindanmaker.com/a/{}"
strCharacterName = "."

if __name__ == "__main__":
	checking_scraper = scraper.Scraper(url.format(str(id)))
	checking_logger = logger.Logger(bPrintOnScreen = True, bOutToFile = True)
	checking_logger.output(checking_scraper.title())
	checking_logger.output(checking_scraper.description())
	while (strCharacterName != ""):
		strCharacterName = input("Input:").strip()
		if strCharacterName == "":
			break
		checking_logger.output(checking_scraper.IO(strCharacterName))
	checking_scraper.close()
