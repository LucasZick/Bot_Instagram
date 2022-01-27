from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Lucas\Desktop\gecko\geckodriver-v0.30.0-win64\geckodriver.exe")
         

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(0.5)
        user_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(3)
        self.curtir_fotos('theHashtagThatYouWantToLike')
    
    def curtir_fotos(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(5)
        for i in range(10):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                time.sleep(3)
                driver.find_element_by_class_name("fr66n").click()
                print('curtido! ')
                time.sleep(16)
            except Exception as e:
                time.sleep(5)
                print('erro!')
                




LucasBot = InstagramBot('@yourUser','@yourPassword')
LucasBot.login()