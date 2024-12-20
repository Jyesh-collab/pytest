import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import json


# @pytest.fixture(scope="function") #annotation & Scope function
# def browser_fun(request): 
#     print("initiating chrome driver") 
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome() 
#     driver.maximize_window()
#     driver.implicitly_wait(20)
#     request.instance.driver = driver
#     driver.maximize_window()

#     yield driver # This will return the driver and ask test to execute the test flow
#     driver.close()


@pytest.fixture(scope="class")  #annotation & Scope class
def browser_cls(request):
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # instanciating Chrome driver inside driver variable
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.maximize_window()

    yield driver # This will return the driver and ask test to execute the test flow

    driver.close()

def pytest_addoption(parser):

    parser.addoption("--browser", action="store", help="input browser to execute")
    parser.addoption("--headless", action="store", help="input browser to execute in headless mod")

@pytest.fixture()
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    params['headless'] = request.config.getoption('--headless')
    return params

@pytest.fixture(scope="function") #annotation & Scope function
def browser_cbt(request, params):
    driver=""
    if params['browser']=='chrome':

        print("initiating chrome driver") 
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome() 
        driver.maximize_window()
        driver.implicitly_wait(20)
        request.instance.driver = driver
        #headless Code
        if params['headless'] == 'true':
            print("Running in headless mode")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(20)
        request.instance.driver = driver

    elif params['browser']=='edge':

        print("initiating edge driver") 
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Edge() 
        driver.maximize_window()
        driver.implicitly_wait(20)
        request.instance.driver = driver
        driver.maximize_window()
    
    else:
        pass

    yield driver # This will return the driver and ask test to execute the test flow
    driver.close()

@pytest.fixture()
def readJson():
    with open('TestData\global.json') as json_file:
         data=json.load(json_file)
    return data
  