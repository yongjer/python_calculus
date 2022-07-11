from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
calculus_questions = [13, 23, 35, 43, 45, 53, 55, 77, 79, 81, 83]
input_question = input("enter the question: ")
input_question = input_question.split(" ")
chromedriver = "./chromedriver"
option = webdriver.ChromeOptions()
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)
driver.get(f"https://www.calcchat.com/book/Calculus-11e/{input_question[0]}/{input_question[1]}/{input_question[2]}/")