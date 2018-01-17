from selenium import webdriver
import os
import datetime


 #fire up selenium
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)

 #import URL's from text file into a list
text_file = open("file.txt")
testArray = text_file.readlines()

#Create new folder named today's date
Today = datetime.date.today()
os.makedirs("/home/mike/test/{0}".format(Today), exist_ok = True)

#loop through the list and take screenshots of every site. Store them in a directory with numerical naming conventions
i=0
while i < len(testArray):
	driver.get(testArray[i])
	driver.get_screenshot_as_file("/home/mike/test/{0}/test{1}.png".format(Today , i))
	i += 1 

#close browser
driver.close()

#pull all directory names from 'test'
FolderContents = os.listdir("/home/mike/test/")

#Loop through list of folder contents and delete directories older than 15 unit(days)

i = 0
while i < len(FolderContents):
	t = datetime.date.today()
	TodaysDate =  t.strftime('%Y-%d-%m')

	TodaysDate = datetime.date.today()
	FolderContents[i] > TodaysDate 
	i += 1