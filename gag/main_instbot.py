from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

DRIVER_PATH = r'E:\BBC\hck\py\gag\chromedriver_win32\chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\WillyFaq\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument('--profile-directory=Default')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)


url = 'https://www.instagram.com/rynkuviceroy/'
driver.get(url)

