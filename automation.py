from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import picamera

# Set WebDrivers
statusDriver = webdriver.Chrome()
pauseDriver = webdriver.Chrome()
resumeDriver = webdriver.Chrome()

# Pull up windows
statusDriver.maximize_window()
pauseDriver.maximize_window()
resumeDriver.maximize_window()
statusDriver.implicitly_wait(20)
pauseDriver.implicitly_wait(20)
resumeDriver.implicitly_wait(20)

# Initialize all windows so they open
statusDriver.get("http://10.13.214.130/rr_status?type=3")
pauseDriver.get("http://10.13.214.130/rr_status?type=3")
resumeDriver.get("http://10.13.214.130/rr_status?type=3")
status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

# Continue to refresh while printer is not printing
while(status != "P"):
	time.sleep(3)
	statusDriver.refresh()
	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

# Stay in this loop as long as we get the Printing status "P"
while(status == "P"):
	time.sleep(2)
	statusDriver.refresh()
	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
	currentLayer = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["currentLayer"]

	# First time it hits 10th layer, set up the drivers
	if(currentLayer == 10):
		# Set the pause driver
		pauseDriver.get("http://10.13.214.130/rr_gcode?gcode=M25")

		# Wait for it to be pausing
		statusDriver.refresh()
		status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Enter this if pause isn't processed immediately
		#while(status != "S"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Now pausing, wait for it to stop (status will turn to "S")
		#while(status == "D"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		resumeDriver.get("http://10.13.214.130/rr_gcode?gcode=M24")
		time.sleep(4) #TODO change this to 10 seconds

		#Take picture here
		print("picture")

		# Stay here while it is resuming
		#while (status == "R"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Wait for it to move on to the next layer before exiting this if
		while (currentLayer % 10 == 0 and currentLayer != 0):
			time.sleep(1)
			statusDriver.refresh()
			status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
			currentLayer = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["currentLayer"]

	# Drivers are set, we can use refresh since it's faster
	if(currentLayer % 10 == 0 and currentLayer != 0):
		# Set the pause driver
		pauseDriver.refresh()

		# Wait for it to be pausing
		statusDriver.refresh()
		status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Enter this if pause isn't processed immediately
		#while (status != "D"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Now pausing, wait for it to stop (status will turn to "S")
		#while (status == "D"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		resumeDriver.refresh()
		time.sleep(4)

		with picamera.PiCamera() as camera:
			camera.resolution = (1280, 720)
			camera.capture("/home/pi/Desktop/test.jpg")
		print("picture")

		# Stay here while it is resuming
		#while (status == "R"):
		#	statusDriver.refresh()
		#	status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]

		# Wait for it to move on to the next layer before exiting this if
		while (currentLayer % 10 == 0 and currentLayer != 0):
			time.sleep(1)
			statusDriver.refresh()
			status = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["status"]
			currentLayer = (json.loads(statusDriver.find_element(By.XPATH, '/html/body/pre').text))["currentLayer"]

statusDriver.close()
pauseDriver.close()
resumeDriver.close()
