from selenium import webdriver
#from getpass import getpass
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://web.whatsapp.com/')

name=input("Enter name of the user or group: ")
msg=input("Enter your message: ")
count=int(input("Enter the number of times you want the message: "))

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box=driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('hnQHL')
    button.click()


