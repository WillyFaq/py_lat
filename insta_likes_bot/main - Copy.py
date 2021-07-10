import configparser
from botinst import *

# DRIVER_PATH = r'E:\BBC\hck\py\whats\chromedriver_win32\chromedriver.exe'
# USERNAME = 'suryagg12'
# PASSWORD = 'apa aja1996'
# PROFILE = 'puputnumita'

config = configparser.RawConfigParser()
config.read('config.cfg')
    
details_dict = dict(config.items('CONFIG'))
botinst = Botinst(details_dict)

botinst.get_config()
botinst.login()

