import os
import json
import requests
from lib.cpdf import save_pdf
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#change path to where you stored chromedriver
# PATH = "/home/pathou/Desktop/selenium/seleniumTest/testSelenium/chromeDriver/chromedriver_linux64/chromedriver"
PATH = "/home/gyanendrokh/RobsonProject/seleniumTest/testSelenium/chromeDriver/chromedriver_linux64/chromedriver"
def selenm():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.accept_untrusted_certs = False
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--start-maximized")
    options.add_argument("--no sandbx")

    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.implicitly_wait(10)

#creating list for website status table
    data = []

    status = ""


#read the dictionary file from text file
    # fname = "webList.txt"
    fname = "dictry.txt"
    wname = {}
    with open(fname) as f:
        for line in f:
            (key, *val) = line.strip().split(',')
            wname[key] = val

#rendering the websites from dictionary
    spce = ""
    error = False
    for web in wname:
        table_data = my_dictionary()
        webname = wname[web]

        host = webname[0]
        instance = webname[1]
        ip = webname[2]
        table_data.add("url",host)
        table_data.add("server", instance)
        table_data.add("ip", ip)

        try:
            driver.get(host)
            status = "Ok"
            table_data.add("status",status)
            data.append(table_data)
            links = driver.find_elements_by_css_selector("a")
            noLinks = len(links)
            # print(links)
            print(noLinks)
            print(host)
        except:
            status = "Down"
            table_data.add("status",status)
            data.append(table_data)
            print('-------',host)

        
        

        # if noLinks <= 1:
        #     error = True
        # else:
        #     pass

    
    print("Data>>>",data)
    if error:
        #create pdf
        # save_pdf(data)
        print("error")
    else:
        print("all working")

    # save_pdf(data)

    r=requests.post('http://localhost:3000/data/getAll',json=data)
    print(";lgkfdwf>>>>",r)

    driver.quit()


class my_dictionary(dict):

  # __init__ function
  def __init__(self):
    self = dict()

  # Function to add key:value
  def add(self, key, value):
    self[key] = value

    
