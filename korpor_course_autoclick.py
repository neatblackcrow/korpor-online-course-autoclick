from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from random import randint

browser = webdriver.Chrome()
browser.get('https://ocsc.chulaonline.net/main/index.asp')

browser.find_element_by_id('uid').send_keys('349910')
browser.find_element_by_id('password1').send_keys('nUNXUnR7rmzzM6r')
browser.find_element_by_css_selector('button[type="button"].btn.btn-danger.btn-round').click()

browser.find_element_by_css_selector('div[style*="#f66b54"] a.two').click()
browser.find_element_by_css_selector('a[href="javascript:oli(\'001M.\',\'teacher\',\'20200930\',\'20210707\')"]').click()


iframe = browser.find_element_by_name('treeFrame')
browser.switch_to.frame(iframe)


course_links = browser.find_elements_by_css_selector('div a')
course_links = [i for i in course_links if not('แบบประเมิน' in i.text)]
[print("index: " + str(index) + " title: " + value.text) for index, value in enumerate(course_links)]

from_index = int(input("Enter start index: "))
to_index = int(input("Enter stop index: "))
min_time = int(input("Enter minimum wait time (sec): "))
max_time = int(input("Enter maximum wait time (sec): "))

# Do while

course_links[from_index].click()
print("Clicked: " + str(from_index) + " " + course_links[from_index].text)
sleep(randint(min_time, max_time))
from_index += 1

while from_index <= to_index:

    course_links[from_index].click()
    print("Clicked: " + str(from_index) + " " + course_links[from_index].text)

    WebDriverWait(browser, 30).until(EC.alert_is_present())
    browser.switch_to.alert.accept();

    sleep(randint(min_time, max_time))
    from_index += 1


# browser.switch_to.default_content()

browser.quit()
