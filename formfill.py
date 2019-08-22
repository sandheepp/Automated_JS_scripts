#pre-requisities: python3.7,pandas


import pandas as pd
import selenium# Using Chrome to access web
from selenium import webdriver
#from selenium.webdriver.firefox.webdriver import WebDriver

df = pd.read_excel('hospital_excel.xlsx')

hospital_names_list = df['Name of Institution']
officer_list = df['Name of Officer']
designation_officer = df['Designation of the officer']
office_landline_number = df['Office land line number']
email = df['Email address']
#print(df)


# Opening the website
#driver = webdriver.Firefox()

driver = webdriver.Chrome()# Open the website
driver.get('https://canvas.case.edu')

# LOGGING IN
# Select the ID 
id_box = driver.find_element_by_id('username')

# Send id information
id_box.send_keys('my_username')

# Find password box
pass_box = driver.find_element_by_name('password')# Send password
pass_box.send_keys('my_password')# Find login button

# Click the login
login_button = driver.find_element_by_name('submit')# Click login
login_button.click()

#Script for Repeated form filling
#Name
pass_box = driver.find_element_by_name('id_name')# Send password
pass_box.send_keys(df[1,1])# Find login button



#find a field and fill in data
pass_box = driver.find_element_by_name('password')# Send password
pass_box.send_keys('my_password')# Find login button


# Click the login button
login_button = driver.find_element_by_name('submit')# Click login
login_button.click()
