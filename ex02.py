from selenium import webdriver
import re

url = input("Enter a URL: ")

driver = webdriver.Chrome("C:/Program Files (x86)/ChromeDriver/chromedriver.exe")
driver.get(url)

# The Email_Regex I'm using was found on this site: https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression
EMAIL_REGEX = r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

list = []

for re_match in re.finditer(EMAIL_REGEX, driver.page_source):
    list.append(re_match.group())

for i, email in enumerate(list):
    print(f'{i + 1}: {email}')

driver.close()
