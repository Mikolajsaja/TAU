import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging


logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('test')


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.amazon.pl/')
temp = driver.find_element(By.ID, 'nav-link-accountList-nav-line-1')

temp.click()
time.sleep(2)
temp = driver.find_element(By.ID, 'ap_email')
temp.send_keys("login")
tempt = driver.find_element(By.ID, 'continue')
tempt.click()
time.sleep(2)
logging.error('Błąd')

driver.close()

#v=EdgeService(verbose=True)
#driverEdge = webdriver.Edge(service=v)
#driverEdge = webdriver.Edge(
#                            EdgeChromiumDriverManager().install())

#driverEdge.maximize_window()
#driverEdge.get('https://www.youtube.com/')
#time.sleep(2)

#obejść cookies

#tempEdge = driverEdge.find_element(By.ID, 'text')
#time.sleep(2)
#tempEdge = driverEdge.find_element(By.ID, 'search')

#tempEdge.send_keys('never gonna give you up')
#time.sleep(20)

#driverEdge.close()
