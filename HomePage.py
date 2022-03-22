from Locators import locators
from element import elements
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class HomePage(elements):
    def __init__(self):
        elements.__init__(self)
        
    def contect_us(self):
        #fills all the fields
        for row in self.csv_file:
            new_dict = dict(row)
            new_dict.pop('lastname')
            for index, x in enumerate(new_dict.items()):
                self.field(locators.contect_us_Locators[index],x[1])
        
            self.driver.find_element(*locators.contect_us_submit_button).click()
        
        #gets the Confirmation
            assert  self.wait.until(EC.presence_of_element_located(locators.constans_us_succsessful))
            self.driver.refresh()
        
    
    def book_room(self):
        for row in self.csv_file:
            new_dict = dict(row)
            new_dict.pop('subject	')
            new_dict.pop('massage')
            self.wait.until(EC.element_to_be_clickable(locators.book_room_button)).click()
            days = self.get_element_of_all_days()
            Unavailables = 0
        
            try: Unavailables = self.get_all_dates_that_are_avilable()
            #If it's a free month then there will not be any "Unavailable" element so it's ok o pass it
            except TimeoutException: pass 
            except: return "falild"
            #fills all the fields
            for index, x in enumerate(new_dict.items()): 
                self.field(locators.book_room_fileds_locators[index],x[1].strip())
            while True:
                #If it's bigger it will be out of index
                if (Unavailables * 3 + 3 ) < len(days):
                    try:
                        #Simple math that gives me the next tree days after the last "Unavailable" element and then "booking it"
                        self.drag_and_drop(days[(Unavailables * 3 )], days[(Unavailables * 3 ) + 1 ] , days[(Unavailables * 3 ) + 3 ])
                        self.driver.find_element(*locators.book_room_submit_button).click()
                        assert self.wait.until(EC.presence_of_element_located(locators.book_room_successful))
                        self.driver.find_element(*locators.book_room_close_button).click()
                        break
                    except: return "falild"
            
                else:
                    try:
                        #All of the month is full so we go next
                        self.driver.find_element(*locators.book_room_next_button).click()
                        Unavailables = self.get_all_dates_that_are_avilable()
                        days = self.get_element_of_all_days()
                    except: return "falild"
            self.driver.refresh()
    
    #This test tries to book a place that was already taken and sees if it blocks the request 
    def book_room_taken(self):
        for row in self.csv_file:
            new_dict = dict(row)
            new_dict.pop('subject	')
            new_dict.pop('massage')
            self.wait.until(EC.element_to_be_clickable(locators.book_room_button)).click()
            days = self.get_element_of_all_days()
            self.drag_and_drop(days[0], days[1] , days[3])
            for index, x in enumerate(new_dict.items()): 
                self.field(locators.book_room_fileds_locators[index],x[1])
        
            self.driver.find_element(*locators.book_room_submit_button).click()
            #result = self.wait.until(EC.presence_of_element_located(locators.book_room_all_alert)).text
            #assert result[:5] == "The r" 
            self.driver.refresh()
