from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random

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

def onWorkBu(date,res):
    # 上班補打卡
    driver.get("http://35.194.135.26/Gaia/public/applyRecord")
    # 日期

    # ((JavascriptExecutor) driver).executeScript("document.getElementsByName('date'[0].removeAttribute('readonly');");
    # WebElement
    # dateFld = driver.findElement(By.id("date_completed"));
    # dateFld.clear();
    # dateFld.sendKeys("date Completed");

    dataPick = driver.find_element(By.XPATH, '//*[@id="day"]')
    dataPick.click()
    # dataPick.send_keys(date)
    dataPick.send_keys(Keys.CONTROL, "a")  # Select all pre-existing text/input value
    dataPick.send_keys(Keys.BACKSPACE)  # Remove that text
    dataPick.send_keys("2022/01/01")
    # 選擇時間
    min = str(random.randint(1,10)).zfill(2)
    driver.find_element(By.XPATH, '//*[@id="type"]').send_keys('上班')
    driver.find_element(By.XPATH, '//*[@id="hour"]').send_keys('9')
    driver.find_element(By.XPATH, '//*[@id="mins"]').send_keys(min)
    # 原因
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[3]/textarea').send_keys(res)
    # driver.close()

def outWorkBu(date,res):
    # 下班補打卡
    driver.get("http://35.194.135.26/Gaia/public/applyRecord")
    # 選擇時間
    min = str(random.randint(11, 25))
    driver.find_element(By.XPATH, '//*[@id="type"]').send_keys('下班')
    driver.find_element(By.XPATH, '//*[@id="hour"]').send_keys('18')
    driver.find_element(By.XPATH, '//*[@id="mins"]').send_keys(min)
    # 原因
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/form/div[3]/textarea').send_keys(res)