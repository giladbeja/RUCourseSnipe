from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

semesterCode = "92023"
desiredIndices = ["07332","07333","07334","19848"]

def handleDriver():
    options = Options()
    options.add_argument("--headless=new")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

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

driver = handleDriver()
while True:
    for ind in desiredIndices:
        url = "https://sis.rutgers.edu/soc/#keyword?keyword="+ind+"&semester="+semesterCode+"&campus=NB&level=U"
        driver.get(url)
        driver.implicitly_wait(3)
        sectionStatus, courseTitle = scrape(driver)
        if sectionStatus:
            print("{} - Index {} is open!, register at https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection={}&indexList={}".format(courseTitle,ind,semesterCode,ind))
