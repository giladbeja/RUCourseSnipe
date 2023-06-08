import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

# courseCode = "01:198:205"
# semester = "9"
# year = "2023"
courseCode = input("Course code: ")
semester = input("First month of semester: ")
year = input("year: ")
url = "https://sis.rutgers.edu/soc/#keyword?keyword="+courseCode+"&semester="+semester+year+"&campus=NB&level=U"

# r = requests.get(url)
# x = r._content
# #x = json.dumps(x)
# print(x)

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
driver.implicitly_wait(5)
totalSections = (driver.find_element(By.CLASS_NAME,"courseOpenSectionsDenominator").text)
totalSections = int(totalSections[3:])
#print(totalSections)
for i in range(1,totalSections+1):
    indexstr = str(i)
    specifystr = str(i-1)
    if(i<10):
        x = driver.find_element(By.ID,courseCode+".0.section0"+indexstr+"."+specifystr+".sectionData.number.span")
    else:
        x = driver.find_element(By.ID,courseCode+".0.section"+indexstr+"."+specifystr+".sectionData.number.span")
    if(x.get_attribute("class")=="sectionopen"):
        print("Section {0} open".format(i))