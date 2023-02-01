from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=s)


def AutoLogin(name,password):
    url = 'http://35.194.135.26/Gaia/public/login'
    driver.get(url)

    if driver.current_url != url:
        return True

    # 帳號
    driver.find_element(By.XPATH,'//*[@id="name"]').send_keys(name);
    # 密碼
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password);
    # 登入
    driver.find_element(By.XPATH,' / html / body / div / div / div[2] / form / button').click()

    if driver.current_url == url:
        return False
    return True


def onWork():
    # 上班
    driver.find_element(By.XPATH, '//*[@id="punchIn"]').click()
    # driver.close()

def outWork():
    # 下班
    driver.find_element(By.XPATH, '//*[@id="punchOut"]').click()
    # driver.close()

