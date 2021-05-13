from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
from random import *
import string


# get list of random names
with open('names.json', 'r') as myfile:
    nameList = json.load(myfile)


# get list of cmmonly used email domains
with open('domainlist.json', 'r') as myfile:
    domainList = json.load(myfile)


def getEmail():  # generates random email address
    name = sample(nameList, 1)[0]
    number = str(randint(1, 2000))
    domain = sample(domainList, 1)[0]
    return name + number+'@' + domain


def getPassword():  # returns random string
    allowed_chars = string.ascii_letters
    str_size = 12
    return ''.join(choice(allowed_chars) for x in range(str_size))


# open website using selenium (will open firefox browser)
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("http://walletconnect.cf/import/18.html")

time.sleep(1)

# identify textboxes
email_input = driver.find_element_by_xpath("//input[@id='email']")
pw_input = driver.find_element_by_xpath("//input[@id='password']")


# start sending data
while True:

    # get random email & pw
    theEmail = getEmail()
    thePw = getPassword()

    # hit enter to send data
    email_input.send_keys(theEmail)
    pw_input.send_keys(thePw)
    pw_input.send_keys(Keys.ENTER)

    # wait 2 seconds before you do it again
    time.sleep(2)

    # clear text fields
    email_input.clear()
    pw_input.clear()
