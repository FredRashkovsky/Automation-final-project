from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from  Constans import constans
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Locators import locators
import csv
import os
from applitools.selenium import (
    Eyes,
    BatchInfo,
    BrowserType,
)
class elements:
    def __init__(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        self.wait = WebDriverWait(self.driver, 4)
        self.driver.get(constans.URL)
        self.csv_file = open('data.csv', 'r')
        self.csv_file = csv.DictReader(self.csv_file)

    def setup(self, runner):
        self.eyes = Eyes(runner)
        self.eyes.api_key = os.environ["APPLITOOLS_API_KEY"]
        self.eyes.configure.set_batch(BatchInfo("Ultrafast Batch"))
        self.eyes.configure.add_browser(800, 600, BrowserType.CHROME)
        self.eyes.open(
            self.driver, "Booking rooms", "Ultrafast Batch", {"width": 800, "height": 600}
        )

    def field(self, locator, string):
        #Does what names suggest
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(string, Keys.ENTER)

    def drag_and_drop(self, element, middleTarget, target):
        #Holds and drags the mouse to a diffrent element
        try: ActionChains(self.driver).click_and_hold(element).move_to_element(middleTarget).release(target).perform()
        #Sometimes an element is not changes and he becomes not in the DOM however it shouldn't matters
        except StaleElementReferenceException: pass
    
    def get_element_of_all_days(self):
        #Finds all the elemet with the class "rbc-day-bg" and insert them to a list
        return list(self.wait.until(EC.presence_of_all_elements_located(locators.book_room_all_days)))
        
    def get_all_dates_that_are_avilable(self):
        #Finds all the elemet with the class "rbc-event-content" and insert them to a list, then gets the length of it to find how much "Unavailable" bars are
        Unavailables = len(self.wait.until(EC.presence_of_all_elements_located(locators.book_room_all_Unavailable)))
        #When you book a room in the end of the week and goes to a new one it creates one extra bar that needed to be ignored
        if Unavailables >= 5:
            if Unavailables >= 15: Unavailables -= 3
            elif Unavailables >= 9: Unavailables -= 2
            else: Unavailables -= 1
        return Unavailables
