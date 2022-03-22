from selenium.webdriver.common.by import By


class locators:
    contect_us_Locators = [(By.XPATH ,'//*[@id="name"]'),
                            (By.XPATH ,'//*[@id="email"]'),
                            (By.XPATH ,'//*[@id="phone"]'),
                            (By.XPATH ,'//*[@id="subject"]'),
                            (By.XPATH ,'//*[@id="description"]')]
    
    contect_us_submit_button = (By.XPATH ,'//*[@id="submitContact"]')
    constans_us_succsessful = (By.XPATH, '//p[contains(text(),"We\'ll get back to you about")]')


    book_room_button = (By.XPATH, "//button[contains(text(),'Book this room')]")
    book_room_next_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div/div[1]/span[1]/button[3]')
    book_room_submit_button = (By.XPATH, "//button[contains(text(),'Book')]")
    book_room_successful = (By.XPATH, "//h3[contains(text(),'Booking Successful!')]")
    book_room_close_button = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/button")
    book_room_all_days = (By.CLASS_NAME, "rbc-day-bg")
    book_room_all_Unavailable = (By.CLASS_NAME, "rbc-event-content")
    book_room_all_alert = (By.XPATH, '//*[@id="root"]/div[2]/div/div[4]/div/div[2]/div[3]/div[5]')

    book_room_fileds_locators = [(By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[1]/input[1]"),
                                  (By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[2]/input[1]"),
                                  (By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[3]/input[1]"),
                                  (By.XPATH, "//body/div[@id='root']/div[2]/div[1]/div[5]/div[1]/div[2]/div[3]/div[4]/input[1]")]
    
