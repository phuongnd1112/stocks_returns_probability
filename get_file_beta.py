from selenium import webdriver 
from time import sleep 

class fileBot(): 
    def __init__(self): 
        self.driver = webdriver.Chrome()

    def openWeb(self): 
        self.driver.get('https://www.investing.com/')

        sleep(5) 

        ##CODE TO TURN OFF THAT STUPID FUCKING AD 
    
    def searchTicker(self): 
        search = self.driver.find_element_by_xpath('/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input')
        search.click() 
        userSearch = input('What is your ticker: ') 
        search.send_keys(str(userSearch)) 
        sleep(5)
        search = self.driver.find_element_by_class_name('js-footer-link')
        search.click()  
    
    def getTicker(self): 
        sleep(5)
        exchanges_list = self.driver.find_elements_by_class_name('fourth')
        for e in exchanges_list: 
            if 'Ho Chi Minh' in e.text:
                e.click()

    def getData(self): 
        sleep(3) 

        historical_select = self.driver.find_element_by_xpath('//*[@id="pairSublinksLevel2"]/li[3]/a')
        historical_select.click()

        sleep(3) 
        
        date_selector = self.driver.find_element_by_xpath('//*[@id="widgetFieldDateRange"]')
        date_selector.click()

        start_date = bot.driver.find_element_by_id('startDate')
        user_start = input('Starting Date in MM/DD/YYYY:')
        start_date.clear()
        start_date.send_keys(user_start)

        end_date = self.driver.find_element_by_id('endDate')
        user_end = input('Ending Date in MM/DD/YYYY:')
        end_date.clear()
        end_date.send_keys(user_end)

        apply = self.driver.find_element_by_xpath('//*[@id="applyBtn"]')
        apply.click()

        download = self.driver.find_element_by_xpath('//*[@id="column-content"]/div[4]/div/a')
        download.click() 

        log_in = self.driver.find_element_by_xpath('//*[@id="loginFormUser_email"]')
        log_in.send_keys(email)

        password_in = self.driver.find_element_by_xpath('//*[@id="loginForm_password"]') 
        password_in.send_keys(passwoord)

        sign_in = self.driver.find_element_by_xpath('//*[@id="signup"]/a')
        sign_in.click() 

        download = self.driver.find_element_by_xpath('//*[@id="column-content"]/div[4]/div/a')
        download.click()

bot = fileBot() 
bot.openWeb() 
bot.searchTicker()
bot.getTicker()  
bot.getData() 




    

