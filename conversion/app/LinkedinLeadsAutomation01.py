# coding: utf-8

import requests
import re
import lxml

from configparser import ConfigParser
from urllib.request import urlopen
from bs4 import BeautifulSoup

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


parser = ConfigParser()
parser.read('/home/ricardo/projects/ireland/app/config/settings.ini')

LINKEDIN_PASSWD = parser.get('linkedin', 'LINKEDIN_PASSWD')
LINKEDIN_NAME = parser.get('linkedin', 'LINKEDIN_NAME')

pagina = urlopen('file:///home/ricardo/projects/ireland/conversion/html/01/01.html')
soup = BeautifulSoup(pagina.read(), 'lxml')
binary = FirefoxBinary('/usr/lib/firefox/firefox')
browser = webdriver.Firefox(firefox_binary=binary)
main_window = browser.current_window_handle
#browser.switch_to_window(main_window)
listadict = []
link_text = ''
count = 0
for a in soup.find_all('a', attrs={'href': re.compile("^https://www.linkedin.com/sales/profile")}):
    link_text = a['href']
    name_text = str(a.text).replace(u'\xa0', u'')  
    count = count + 1
    listadict.append ({'id': count, 'name': name_text, 'link': link_text})

d = listadict[4]
d["id"]
d["name"]
d["link"]

browser.get(d["link"])

linkedin_name = LINKEDIN_NAME
field_name = browser.find_element_by_xpath("//*[@id='session_key-login']")
field_name.send_keys(linkedin_name)

linkedin_password = LINKEDIN_PASSWD
field_name = browser.find_element_by_xpath("//*[@id='session_password-login']")
field_name.send_keys(linkedin_password)

buttonSign = browser.find_element_by_xpath("//*[@id='btn-primary']")
buttonSign.click()

browser.get_screenshot_as_file(d["name"] + '.png')

browser.execute_script("document.getElementsByClassName('connect primary top-card-action ember-view')[0].click()")

browser.execute_script("document.getElementsByClassName('button-secondary-large')[0].click()")

#driver.execute_script("document.getElementsByClassName('send-invite__custom-message mb3 ember-text-area ember-view').send_keys('Hi,')")

browser.execute_script("document.getElementById('custom-message').send_keys('text')")

# driver.execute_script("document.getElementsByClassName('button-primary-large ml3')[0].click()")

# buttonConnect.click()

#<button id="ember1585" class="connect primary top-card-action ember-view">  
#<span class="default-text">Connect</span>
#<span class="success-text">Pending</span>
#<span class="success-text-long">Invitation Sent</span>
#</button>
# browser.find_element_by_xpath('just copy and paste the Xpath').click()

#<button class="button-secondary-large" data-ember-action="" data-ember-action-6097="6097">
#            Add a note
#          </button>

#<textarea name="message" placeholder="Ex: We know each other from…" maxlength="300" id="custom-message" class="send-invite__custom-message mb3 ember-text-area ember-view"></textarea>
#<button class="button-primary-large ml3" data-ember-action="" data-ember-action-6112="6112">
#            Send invitation
#          </button>

# XPATH

# linkedin name
# //*[@id="session_key-login"]
# linkedin_name = ricardoportela@workflowict.com

# linkedin_password = Doda7970
# //*[@id="session_password-login"]

# Linkedin Sing in button
# //*[@id="btn-primary"]


# CONNECT BUTTON
# //*[@id="ember1524"]

# ADD A NOTE
# //*[@id="ember2204"]/div[1]/div/section/div/div[2]/button[1]

# SEND INVITATION
# //*[@id="ember2204"]/div[1]/div/section/div/div[2]/button[2]
