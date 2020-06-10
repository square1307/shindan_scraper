#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

class Scraper:
	def __init__(self,url=""):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--incognito")
		self.url = url
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		self.min_window()
		if url != "":
			self.driver.get(self.url)

	def min_window(self):
		self.driver.minimize_window()

	def title(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[1]/div[2]/h1/a')[0].text
		return result

	def description(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div[1]/div[3]')[0].text
		return result
	
	def changeURL(self,url):
		try:
			self.url = url
			self.driver.get(self.url)
			return True
		except:
			return False
	
	def submitInput(self,input):
		self.clearInput()
		self.driver.find_elements_by_xpath('//*[@id="form"]/input[1]')[0].send_keys(input)
		self.driver.find_elements_by_xpath('//*[@id="shindan_submit"]')[0].click()
	
	def result(self):
		result = self.driver.find_elements_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[1]/div[2]/div')[0].text
		return result
	
	def previousPage(self):
		self.driver.back()
		self.clearInput()

	def clearInput(self):
		self.driver.find_elements_by_xpath('//*[@id="form"]/input[1]')[0].clear()

	def IO(self,input):
		self.submitInput(input)
		time.sleep(0.2)
		result = self.result()
		return result
	
	def screenshot(self,date,strname,strurlid):
		try:
			os.mkdir(date)
		except:
			pass
		page_width = self.driver.execute_script('return document.body.scrollWidth')
		page_height = self.driver.execute_script('return document.body.scrollHeight')
		self.driver.set_window_size(page_width, page_height/2)
		self.driver.save_screenshot('{}/{}_{}_{}.png'.format(date,date,strname,strurlid))
		
	def close(self):
		self.driver.close()