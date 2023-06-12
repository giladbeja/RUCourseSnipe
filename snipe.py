from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from alert import alert
import time

#Customize with relevant information to individual case
semesterCode = "" #first month of semester followed by year, i.e. 92023 would be Fall 2023
desiredIndices = [""] #add any indices of sections which you want to snipe
phoneNumber = ""+"@txt.att.net" #put phone number in the first set of quotations
email = ""
resetInterval = 7200 #Once notified, the index will no longer be in the desired list, after x amount of seconds, it will be re-added in case the opportunity was missed to register
#####################
def handleDriver():
    options = Options()
    options.add_argument("--headless=new")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
#####################
def scrape(driver):
    driver.refresh()
    try:
        open = driver.find_element(By.CLASS_NAME,"sectionopen")
        status = True
    except:
        status = False
    if(status):
        courseTitle = driver.find_element(By.CLASS_NAME,"highlighttext").text
        return True, courseTitle
    return False, 0
#####################
notiftime = 0
notified = []
driver = handleDriver()
while True:
    if(time.time()-notiftime>7200):
        desiredIndices.extend(notified)
        notified = []
    for ind in desiredIndices:
        url = "https://sis.rutgers.edu/soc/#keyword?keyword="+ind+"&semester="+semesterCode+"&campus=NB&level=U"
        driver.get(url)
        driver.implicitly_wait(3)
        sectionStatus, courseTitle = scrape(driver)
        if sectionStatus:
            notified.append(ind)
            desiredIndices.remove(ind)
            notiftime = time.time()
            print("{} - Index {} is open!, register at https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection={}&indexList={}".format(courseTitle,ind,semesterCode,ind))
            alert("Snipe available!", "{} - Index {} is open! register at https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection={}&indexList={}".format(courseTitle,ind,semesterCode,ind),phoneNumber)
            alert("Snipe available!", "{} - Index {} is open! register at https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection={}&indexList={}".format(courseTitle,ind,semesterCode,ind),email)
