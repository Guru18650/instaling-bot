from genericpath import isfile
import json 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
if(isfile('login.json') == False):
    c = {"login":"","pass":""}
    print("Podaj login")
    c["login"] = input()
    print("Podaj hasło")
    c["pass"] = input()
    with open("login.json", "w") as outfile:
        json.dump(c, outfile)
u = open('login.json', encoding='utf-8')
u = json.load(u)
f = open('data.json', encoding='utf-8')
data = json.load(f)
driver = webdriver.Chrome()
driver.get("https://instaling.pl/teacher.php?page=login")
driver.implicitly_wait(0.5)
login_box = driver.find_element(by=By.NAME, value="log_email")
password_box = driver.find_element(by=By.NAME, value="log_password")
s = driver.find_elements(By.TAG_NAME, "button")
login_box.send_keys(u["login"])
password_box.send_keys(u["pass"])
s[1].click()
a = driver.find_elements(By.TAG_NAME, "a")
a[2].click()
s2 = driver.find_element(By.XPATH, "//*[@id=\"start_session_button\"]/h4")
s2.click()
while 1==1:
    time.sleep(0.2)
    t = driver.find_element(By.XPATH, "//*[@id=\"question\"]/div[2]/div[2]").text
    answer = driver.find_element(by=By.XPATH, value="//*[@id=\"answer\"]")
    a = data.get(t, "0")
    if(a=="0"):
        case3 = driver.find_element(by=By.XPATH, value="//*[@id=\"dont_know_new\"]")
        case3.click()
        case4 = driver.find_element(by=By.XPATH, value="//*[@id=\"skip\"]")
        case4.click()
    else:
        answer.send_keys(a)
        case = driver.find_element(by=By.XPATH, value="//*[@id=\"check\"]")
        case.click()
        case2 = driver.find_element(by=By.XPATH, value="//*[@id=\"nextword\"]")
        case2.click()
