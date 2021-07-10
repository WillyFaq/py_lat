from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  
import time


class Botinst:

	DRIVER_PATH = ''
	USERNAME = ''
	PASSWORD = ''
	PROFILE = ''

	def __init__(self, config):
		self.DRIVER_PATH = config["driver_path"]
		self.USERNAME = config["username"]
		self.PASSWORD = config["password"]
		# driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)
		# driver.get("http://www.instagram.com/")
		# wait = WebDriverWait(driver, 600)
		self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)
		self.driver.get("http://www.instagram.com/")
		self.wait = WebDriverWait(driver, 600)

	def login(self):
		# driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)
		# driver.get("http://www.instagram.com/")
		# wait = WebDriverWait(driver, 600)

		# <input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value="suryagg12">
		uname_path = '//input[@aria-label="Phone number, username, or email"]'
		inp_uname = self.wait.until(EC.presence_of_element_located((By.XPATH, uname_path)))
		inp_uname.send_keys(USERNAME)

		# <input aria-label="Password" aria-required="true" autocapitalize="off" autocorrect="off" name="password" type="text" class="_2hvTZ pexuQ zyHYP" value="apa aja1996">
		pass_path = '//input[@aria-label="Password"]'
		inp_password = self.wait.until(EC.presence_of_element_located((By.XPATH, pass_path)))
		inp_password.send_keys(PASSWORD + Keys.ENTER)

		# <button class="sqdOP yWX7d    y3zKF     " type="button">Not Now</button>
		# <span class="coreSpriteKeyhole"></span>
		btnwait_path = '//span[@class="coreSpriteKeyhole"]'
		btn_btnwait = self.wait.until(EC.presence_of_element_located((By.XPATH, btnwait_path)))


	def get_config(self):
		print(self.DRIVER_PATH)
		print(self.USERNAME)
		print(self.PASSWORD)
