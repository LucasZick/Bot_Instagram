#TO RUN THIS YOU WILL NEED TO PUT YOUR GECKODRIVER, PYTHON, AND MAYBE THE VSCODE ON YOUR WINDOWS PATH, THATS REALLY EZ IN WINDOWS 10-11, JUST TRY SEARCHING ON THE INTERNET
#YOU WILL NEED THE SELENIUM TO RUN THE CODE, MAKE SURE THAT YOU ALREADY HAVE IT INSTALLED
#YOU NEED TO ADAPT THE CODE TO YOUR ACCOUNT, CHANGE THE BLOCKS IN THE LINES 13, 28 AND 27 TO CONFIGURE IT TO YOUR OWN STYLE
#YOU CAN ALSO CHANGE THE PARAMETER TO THE 'RANGE' FUNCTION ON THE LINE 43 TO CHOOSE HOW MUCH TIMES IT WIL GET DOWN AND LOAD MORE POSTS
#IF YOUR NETWORK CONNECTION ISN'T GOOD ENOUGH FOR THE 'TIME.SLEEP(X)'s USED HERE, YOU CAN CHANGE TO HIGHER VALUES TO GIVE IT SOME MORE TIME, OR THE INVERSE FOR GOOD CONNECTIONS
#DO NOT CHANGE THE 18 SECONDS VALUE OF THE LIKE DELAY, IT WILL PROBABLY GIVE U A INSTAGRAM BLOCK, IT NEED TO LOOK LIKE A HUMAN INTERACTION
#THE AVERAGE LIKED PUBS THAT INSTAGRAM IS ALLOWING DAILY IS SOMETHING LIKE 200-220
#THIS CODE IS INSPIRED IN THIS VIDEO 'https://www.youtube.com/watch?v=0PdIP2Q2X4U'. MAKE SURE TO LIKE IT IF YOU ENJOYED THIS BOT



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username , password):#constructor
        self.username = username
        self.password = password                                                        #DONT FORGET TO CHANGE THAT
        self.driver = webdriver.Firefox(executable_path=r"path to your geckodriver.exe location(ex:C:\Users\User\Desktop\gecko\geckodriver-v0.30.0-win64\geckodriver.exe)")#define gecko as the driver
 

    def login(self):
        driver = self.driver #managing the geckodriver to a local variable
        driver.get('https://www.instagram.com')#define the link
        time.sleep(0.5)#wait the page to load
        user_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')#login input path
        user_element.clear()#clear login
        user_element.send_keys(self.username)#write the user
        password_element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')#password input path
        password_element.clear()#clear password
        password_element.send_keys(self.password)#write the password
        password_element.send_keys(Keys.RETURN)#press the ENTER key
        time.sleep(3)#wait the page to load
        self.like_posts('@HashtagThatYouWantToLike')


    def like_posts(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')#search the link of the hashtag
        time.sleep(5)#wait the page to load
        for i in range(10):#scroll the page to the bottom X times to load more posts
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)
        hrefs = driver.find_elements_by_tag_name('a')#catch every post
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))#show how much posts have been saved

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')#scroll to the bottom of the page
            try:
                time.sleep(1)
                now = time.strftime("%H:%M:%S")#save the time
                driver.find_element_by_class_name("fr66n").click()#click the like button
                print('liked! at ' + now)#show the confirmation and the time
                time.sleep(18)#wait to restart the cycle
            except Exception as e:
                print('error! at '+ now)#show the fail and the time
                time.sleep(5)#wait to retry
                

LucasBot = InstagramBot('@yourUser','@yourPassword')#define the bot and it's parameters 
LucasBot.login()#excute the bot