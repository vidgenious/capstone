from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

statusDriver = webdriver.Chrome()
pauseDriver = webdriver.Chrome()
resumeDriver = webdriver.Chrome()

statusDriver.maximize_window()
pauseDriver.maximize_window()
resumeDriver.maximize_window()
statusDriver.implicitly_wait(20)
pauseDriver.implicitly_wait(20)
resumeDriver.implicitly_wait(20)

statusDriver.get("http://10.13.214.130/rr_status?type=3")
pauseDriver.get("http://10.13.214.130/rr_gcode?gcode=M25")
status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
resumeDriver.get("http://10.13.214.130/rr_gcode?gcode=M24")
statusDriver.refresh()
status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
print(type(status));

while(status != "P"):
	print("in Here")
	statusDriver.refresh()
	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

while(True):
	statusDriver.refresh()
	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

	while(status == "P"):
	    statusDriver.refresh()
	    status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
	    currentLayer = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["currentLayer"]

	    if(currentLayer % 10 == 0 and currentLayer != 0):
	        pauseDriver.refresh()
	        while(status == "D"):
	            statusDriver.refresh()
	            status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
        
	        resumeDriver.refresh()
	        time.sleep(4)
	        #Take picture here
	        while(status == "R"):
	            statusDriver.refresh()
	            status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
            
	        while(currentLayer % 10 == 0 and currentLayer != 0):
	            statusDriver.refresh()
	            currentLayer = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["currentLayer"]
        







statusDriver.close()
