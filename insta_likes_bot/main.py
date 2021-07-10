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

DRIVER_PATH = r'E:\BBC\hck\py\whats\chromedriver_win32\chromedriver.exe'
USERNAME = 'suryagg12'
PASSWORD = 'apa aja1996'
PROFILE = 'willyfaq'

def init():
	driver = webdriver.Chrome(executable_path=DRIVER_PATH)
	driver.get("http://www.instagram.com/")
	wait = WebDriverWait(driver, 600)
	login(driver, wait)
	like_by_profile(driver, wait, PROFILE)
	driver.quit()

def login(driver, wait):
	uname_path = '//input[@aria-label="Phone number, username, or email"]'
	inp_uname = wait.until(EC.presence_of_element_located((By.XPATH, uname_path)))
	inp_uname.send_keys(USERNAME)

	pass_path = '//input[@aria-label="Password"]'
	inp_password = wait.until(EC.presence_of_element_located((By.XPATH, pass_path)))
	inp_password.send_keys(PASSWORD + Keys.ENTER)
	
	btnwait_path = '//span[@class="coreSpriteKeyhole"]'
	btn_btnwait = wait.until(EC.presence_of_element_located((By.XPATH, btnwait_path)))

def get_post(driver, wait, user):
	driver.get(f"https://www.instagram.com/{user}/");
	wait = WebDriverWait(driver, 600)

	article_path = '//article[@class="ySN3v"]'
	article = wait.until(EC.presence_of_element_located((By.XPATH, article_path)))

	last_height = driver.execute_script("return document.body.scrollHeight")
	post_l = {}
	while True:
		images_box = article.find_elements_by_class_name('v1Nh3')
		for img in images_box:
			a = img.find_element_by_tag_name('a')
			src = a.get_attribute("href")
			post_l[src] = src
			
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
	return post_l


def like_by_profile(driver, wait, user):
	posts = get_post(driver, wait, user)
	jml = 1
	for p in posts:
		# print(p)
		driver.get(p);
		wait = WebDriverWait(driver, 600)
		like_path = '//span[@class="fr66n"]'
		# like_btn = driver.find_element_by_xpath(like_path)
		like_btn = wait.until(EC.presence_of_element_located((By.XPATH, like_path)))
		like_btn.click()
		print(f' {p} --> LIKED ({jml} of {len(posts)})')
		jml += 1
		time.sleep(3)


if __name__ == '__main__':
	init()