#! Python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class NewPost:
    def __init__(self, user, passwd):
        """ init method to set the initial parameters
        Returns an open Firefox browser
        """
        self.browser  = webdriver.Firefox()
        self.browser.get("http://www.facebook.com")
        self.__user = user
        self.__passwd = passwd
        self.username = self.browser.find_element_by_id("email")
        self.password = self.browser.find_element_by_id("pass")
        self.submit   = self.browser.find_element_by_id("u_0_b")

    def __str__(self):
        return "Class to post sentences on Facebook"

    def insertCredential(self):
        """ Inserts the credentials to get into the fb account
        Returns a browser logged into a fb account
        """
        self.username.send_keys(self.__user)
        self.password.send_keys(self.__passwd)
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
        self.send = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div")
        sleep(1)
        self.send.click()
        sleep(2)

    def run(self, msg):
        """ Runs the methods in the right order
        Returns the complete pipeline
        """
        self.insertCredential()
        self.sendMsg(msg)
        self.browser.quit()

