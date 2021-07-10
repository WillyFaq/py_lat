from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

DRIVER_PATH = 'chromedriver_win32/chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\WillyFaq\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)


def waiting_func(by_variable, attribute):
    print("waitingg....")
    try:
        WebDriverWait(driver, 20).until(lambda x: x.find_element(by=by_variable,  value=attribute))
        print("DONE")
    except (NoSuchElementException, TimeoutException):
        print('{} {} not found'.format(by_variable, attribute))
        exit()

"""
driver.get('https://9gag.com/gag/aAe9XMp')
waiting_func('class name', 'up')
vote = driver.find_element_by_class_name('up')
vote.click()

driver.get('https://9gag.com/gag/aP72VOB')
waiting_func('class name', 'up')
vote = driver.find_element_by_class_name('up')
vote.click()
"""

# pos = ["aj84bmw", "a3QOoYe", "aPRmVWV", "aXjNe7P", "ayo4zNy", "aAgEvmd", "a3RANZ3", "a5RB5Vq", "aY7OAXO", "aO04R3N", "aQ1Q2e2", "ao5VLYg", "aEgVojO", "a9RvvKK", "aEgV0BM", "ap5DN1M", "ad5QLXj", "aDgbK4G", "aO07oZM", "aWEbvwK", "a5R5EKG", "aR0NGxj", "aR0NG6Q", "a2RjjzO", "am5bpZX", "arorBv7", "aZ7V2Np", "a4RynLy", "ayowNDX", "aXj1n19", "ayoKO1b", "a4ROOYv", "aBgBjVz", "avoYoYW", "aO7ovOM", "arV15ny", "a8GdYbV", "an4eBOL", "a9njbEK", "a7W52nq", "aO7q1E6", "aBmKEnO", "aQdqoOz", "azmb2Dx", "aj9rgYw", "a8GWE0V", "a3wYRR5", "a3wYK25", "aK7z6B6", "a1WdYLv", "aLwDMr6", "an49nKz", "aZyDwrz", "a7Wq0rL", "a1Wm54b", "aEP0oXK", "a9ny0P0", "aLwnozA", "ax9y8d1", "aK7GXWN", "aeD9q1W", "aP7ALYR", "aXgPzYV", "amvowz4", "aBmZPKA", "a0No0bL", "aR7Lzvj", "aLwLLrz", "aO724Yv", "aeD4OWm", "a5WVwMG", "a7W8e4q", "avzW14b", "a0NoVWZ", "aLwLemA", "amvWG2o", "amvWoM6", "aGdLW2X", "aBm61DA", "aQdvxnz", "aVwoXGP", "a9n6LGK", "aBm6YAA", "a7WOypb", "aK7AP81", "aoP392x", "aQdv4pd", "aeD1Nmj", "aBm6wEA", "apG32e5", "aR743WB", "aK7A7gO", "awB3gOy", "aGdny9X", "a5W6Qnq", "awB3yoW", "ax93yYW", "an4Rg6L", "an4Rz1q", "aP7mA3Q", "aXgMdb6", "aqnXB2Y", "aLwzWvW", "abG1EpX", "ax93mKD", "aZy1RX9", "aqnXYpL", "ax93YxK", "aQdv25d", "an4nQoE", "ax9vM12", "a8GmE9Y", "ax9v9pn", "abGOVgr", "aZywyo6", "agAOBgK", "aBmLddA", "avze5W5", "aYyO732", "azmPmgp", "a8GmKbO", "aR7Z2dA", "aBmLXmz", "aO741xM", "abGOBN9", "an4nEwb", "aK79eZQ", "aXgNWKz", "aye4RZX", "amvGM5o", "a2W82ve", "a6K92p9", "an4nEGB", "an4npdB", "a43Npq6", "abG43pL", "agAOMMn", "a8GmPMp", "awBmqO4", "aK79rZ1", "a1WD9NR", "aEPVr4p", "aeDOL4m", "aeDZRwm", "a9n5BMD", "aeDZ7YB", "aye6vYb", "aYyDmZv", "agA7E96", "ax96Pjp", "abGWVZ9", "aNgVp2r", "aWxvjAq", "apGPNEp", "a8GD5o6", "aBmP0pO", "aD4Zdb7", "a3wy2O8", "adVneRM", "a2WyDxD", "a9n8my6", "a435Ap1", "a2Wy85E", "aO7D4ZN", "a5WGB7L", "aP7884V", "aAe4KWL", "a43565d", "avzEW15", "aO7D2gD", "a7WVq6r", "azmG5Lm", "aGdMEQ7", "aP78n3V", "awBLvb8", "amvmnOV", "a0Nn8Az", "aGdM3o5", "agA8MZK", "a1WLKeD", "aNgRWwA", "a1WLBqG", "avzvVDM", "aWx2PL4", "aR729Xq", "amvVRO6", "an4DD1V", "aO71GVM", "a9nX2QZ", "aVw22oO", "aGdOvMw", "amvpbbo", "a3wbDDm", "arV29qK", "adVobqM", "abGQP8r", "aXgKy4b", "aGd7RgX", "a8GVbYe", "a5W5dXG", "aeDR37Q", "a1WOvw8", "aXgR0xg", "a5W5pvg", "abGR5x9", "a43wpK1", "aeDWKyb", "ax9mxKn", "aAem0eR", "a43x15d", "aR7yrz2", "abGdgGp", "a5Wx1Qr", "aAembnd", "ax9AMVK", "agAZoWg", "aeDPg6O", "aqnpnov", "aLwNpr6", "ayeVM08", "avzX5Gd", "an4W5Wn", "avzXvLn", "agAZ8Pr", "aXgGV8D", "aoPqxZg", "aBmNP5z", "aVw1m4v", "amvbmnX", "avzXEqM", "aD4NnLw", "abGmWg9", "an4WvEE", "an4W2m0", "a1WqDOY", "a1WqmQP", "aVw1xV8", "agAZ6P6", "a1Wqx1b", "azmDQRm", "aNg23db", "a1WqwMw", "aAeN59L", "aVw19M2", "aeDPz75", "a1WqjVG", "aNg2MBw", "aGdNQ2n", "aK7nd3Z", "a3weAVr", "apGzD3E", "a9nZ6Pm", "aVw4E6d", "a6K4XoR", "amvK4mj", "aZyoY0X", "a1WB69P", "a43mMjA", "aR79xBA", "a5Wvm3o", "aD4rBM9", "adVWyE9", "aR78Qg7", "ax9edwp", "aAeLRdR", "aeDqKXj", "aLwORQ5", "aNgGgNr", "azmvm5p", "amvOvbV", "amvOBy2", "a6KeOnN", "a3wzR57", "aVw9YRK", "aWxe1dA", "a5W9nQE", "a1W8Qqw", "azmv9Gz", "aBmbxmP", "aEPjB89", "abGLzNE", "amvOr3y", "aNgGzbG", "abGLpAL", "aK7XjwN", "agApqjr", "aR78KR5", "aEPj79p", "awB9VQ8", "arVDRr5", "aP7VWZK", "a5W9K0E", "aoPGjm3", "apGnBRM", "aWxeON6", "apGno1p", "aXgmEvv", "an40YoV", "a1W8AzY", "avzBE3n", "aD4LZEd", "a438NBQ", "a2WVyOD", "aP70oEG", "agAb7BK", "a5WAGMq", "aD4L88N", "a1Wn53G", "a2WVDYE", "aEPbVRx", "a2WVweY", "a2WVwjE", "azmzd9b", "avzV6Rn", "a6Kz9w8", "a3wD5G1", "ayeAN5r", "aO7Oxg3", "apGXRpb", "a2WVvod", "awBDyrr", "aVw8boM", "aP70ABR", "aXgzDXD", "a1Wn4Bw", "aQdKwZq", "aeDEvYm", "aeDEo7b", "adVMmLD", "aQdK0EK", "aVw8y7v", "amvyZ59", "a7WBgxA", "a3wDOBe", "aAe7ADp", "aEPbKAK", "aZyXPA3", "aD490b9", "a7WgvP2", "a43g9Qy", "aBmz91Q", "an4Zq6b", "aBmz9xO", "aWxyZWA", "a0Njozd", "a9nwLZ1", "aP7L48g", "a1WgeVv", "aAeArBE", "aj9v6ZG", "aWxy64d", "a43gdDA", "agAbpyv", "aO7O1b2", "amvQ8G6", "aNgMnz6", "awBj7Oy", "a9nwPK1", "azmyLpB", "aoPo0Zm", "a7WgK0L", "aoPo05g", "aAeApLL", "aEP5D3K", "a2WpD1Y", "azmwK0B", "aMx5nb6", "aLw5AmV", "aP7280P", "azmwOMm", "aK759zN", "a9n0vq0", "aVw5KLn", "aLw5GMv", "arVw3Dd", "a0Nq0pd", "aoPwRZx", "aAe5QG9", "aEP5VLK", "ayew4nY", "avzweRX", "aLw5LAg", "aAe5Q60", "a1Wj08w", "aD45697", "a2WpM29", "aBm5ZvP", "aWx5nzZ", "aoPw6Zw", "a9n04wj", "apGwnPE", "a9n04QL", "a2WpAmw", "aVw51rK", "azmwo5p", "abGwm1X", "aqnwpxY", "aeDwPoO", "aVw59mK", "aNg5qQv", "a9nGq1D", "awBpZY8", "an4oOqn", "amvZAO4", "a43011A", "aK7ME0N", "arVLMP6", "a5WYE1L", "aD4v2yB", "aWxXgEn", "a7WxWGz"]
# for x in pos:
# 	#print(x)
# 	url = 'https://9gag.com/gag/'+x
# 	driver.get(url)
# 	waiting_func('class name', 'up')
# 	vote = driver.find_element_by_class_name('up')
# 	vote.click()
# 	time.sleep(2)


url = 'https://www84.zippyshare.com/v/tLbmh3b4/file.html'
driver.get(url)
waiting_func('class name', 'center')
down = driver.find_element_by_id('dlbutton')
down.click()
print(down)
