from selenium import webdriver

try:
    driver = webdriver.Chrome('chromedriver')
    url = 'https://www.google.com.tw'
    driver.get(url)
except Exception as e:
    print(e)
# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')


