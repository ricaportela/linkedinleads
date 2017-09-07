
# coding: utf-8
from  leadsapp.models import Linkedinleads

import selenium.webdriver.support.ui as ui
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

def main():
     parser = ConfigParser()
     parser.read('/home/ricardo/projects/ireland/conversion/app/config/settings.ini')

     LINKEDIN_PASSWD = parser.get('linkedin', 'LINKEDIN_PASSWD')
     LINKEDIN_NAME = parser.get('linkedin', 'LINKEDIN_NAME')

     binary = FirefoxBinary('/usr/lib/firefox/firefox')
     browser = webdriver.Firefox(firefox_binary=binary)
     main_window = browser.current_window_handle
     #browser.switch_to_window(main_window)

     leads_list = Linkedinleads.objects.order_by('id')

     link = leads_list[1].link

     browser.get(str(link))

     linkedin_name = LINKEDIN_NAME
     field_name = browser.find_element_by_xpath("//*[@id='session_key-login']")
     field_name.send_keys(linkedin_name)

     linkedin_password = LINKEDIN_PASSWD
     field_name = browser.find_element_by_xpath("//*[@id='session_password-login']")
     field_name.send_keys(linkedin_password)

     buttonSign = browser.find_element_by_xpath("//*[@id='btn-primary']")
     buttonSign.click()


     # simulates push connect button
     browser.execute_script("document.getElementsByClassName('connect primary top-card-action ember-view')[0].click()")
     browser.execute_script("document.getElementsByClassName('button-secondary-large')[0].click()")

     mytext = "Hi, "+  leads_list[1].name +", I am an experienced Cobol and Python developer ."
     #mytext = mytext + "Recently, I am working as a Researcher Scientist for the SEIP 7 in Brazil where he develops monitoring systems to the Oil industry."
     mytext = mytext + "I\'m looking for employment permit in Ireland as I believe my experience with software is an asset in this Country. Let\'s connect?"


     # this line I'll put the text
     invitation = browser.find_element_by_id("custom-message")
     #browser.execute_script(objtext)
     invitation.send_keys(mytext)
     # buttonConnect.click()


if __name__ == ("__main__")
    main()
