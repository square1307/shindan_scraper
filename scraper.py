#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

import subprocess

class Scraper:
	def __init__(self,url):
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		self.driver = webdriver.Chrome(options=options)
		#self.driver.minimize_window()
		self.driver.get(url)

	def title(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[1]/div[2]/h1/a')[0].text
		return result

	def description(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[1]/div[3]/span')[0].text
		return result
	
	def submitInput(self,input):
		self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div[1]/div/form/input[1]')[0].send_keys(input)
		self.driver.find_elements_by_xpath('//*[@id="shindan_submit"]')[0].click()
	
	def result(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div')[0].text
		return result
	
	def previousPage(self):
		self.driver.back()

	def clearInput(self):
		self.driver.find_elements_by_xpath('//*[@id="form"]/input[1]')[0].clear()

	def IO(self,input):
		self.submitInput(input)
		time.sleep(0.2)
		result = self.result()
		self.previousPage()
		self.clearInput()
		return result
	
	def close(self):
		self.driver.close()
		subprocess.check_output(['pkill','-9', 'chromedriver'], stderr=subprocess.STDOUT)