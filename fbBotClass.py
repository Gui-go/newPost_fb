from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import yaml


class NewPost:
    def __init__(self, user, passwd):
        """ init method to set the initial parameters
        Returns an open Firefox browser
        """
        self.browser  = webdriver.Firefox()
        self.browser.get("http://www.facebook.com")
        self.user = user
        self.passwd = passwd
        self.username = self.browser.find_element_by_id("email")
        self.password = self.browser.find_element_by_id("pass")
        self.submit   = self.browser.find_element_by_id("u_0_b")

    def insertCredential(self):
        """ Inserts the credentials to get into the fb account
        Returns a browser logged into a fb account
        """
        self.username.send_keys(self.user)
        self.password.send_keys(self.passwd)
        self.submit.click()
        sleep(3)

    def sendMsg(self, msg):
        """ Finds the post element, insets the message and send it
        Returns the browser with the task completed
        """
        self.minding = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div")
        sleep(2)
        self.minding.send_keys(" ")
        sleep(3)
        self.minding.send_keys(msg)
        sleep(1)

    def run(self, msg):
        """ Runs the methods in the right order
        Returns the complete pipeline
        """
        self.insertCredential()
        self.sendMsg(msg)
        self.browser.quit()

