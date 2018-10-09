# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:44:51 2018

@author: alihan.zihna

@description:	this script just fills some of the fields for GNIB-IRP Ireland applications.(For work-visa + renewal) This is a quick and dirty app, it doesn't interact with the date fields and by the time that I wrote it, it got captcha questions to verify as bot. But still way faster than inputting all the information again and again. It doesn't submit the form automatically. 
"""

from selenium import webdriver
from selenium.webdriver.common import keys


browser = webdriver.Chrome(executable_path="C:\chromedriver")

browser.get('https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/AppSelect?OpenForm')

category = browser.find_element_by_id('Category')
category.send_keys(keys.Keys.ARROW_DOWN)
category.send_keys(keys.Keys.ARROW_DOWN)
category.send_keys(keys.Keys.ARROW_DOWN)

subcategory = browser.find_element_by_id('SubCategory')
subcategory.send_keys(keys.Keys.ARROW_DOWN)


confirmGNIB = browser.find_element_by_id('ConfirmGNIB')
confirmGNIB.send_keys(keys.Keys.ARROW_DOWN)



# Change the GNIB ID
GNIBNo = browser.find_element_by_id('GNIBNo')
GNIBNo.send_keys('XXXXX')



# Change the name
GivenName = browser.find_element_by_id('GivenName')
GivenName.send_keys('ZZZZZZZZZ')

# Change surname
SurName = browser.find_element_by_id('SurName')
SurName.send_keys('YYYYYYYYY')

# Change nationality
Nationality = browser.find_element_by_id('Nationality')
Nationality.send_keys('Turkey')


# change email
Email = browser.find_element_by_id('Email')
Email.send_keys('XXXXXXXX')


EmailConfirm = browser.find_element_by_id('EmailConfirm')
EmailConfirm.send_keys('XXXXXXXXX')



FamAppYN = browser.find_element_by_id('FamAppYN')
FamAppYN.send_keys(keys.Keys.ARROW_DOWN)
FamAppYN.send_keys(keys.Keys.ARROW_DOWN)
FamAppYN.send_keys(keys.Keys.ENTER)



PPNoYN = browser.find_element_by_id('PPNoYN')
PPNoYN.send_keys(keys.Keys.ARROW_DOWN)
PPNoYN.send_keys(keys.Keys.ENTER)

# change the passport no
PPNo = browser.find_element_by_id('PPNo')
PPNo.send_keys('XXXXXXXXXXX')





