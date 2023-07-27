from pytest import fixture
from pytest import mark
import json
import time
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

my_jsonpath = "./data/test_data.json"


def load_jsondata(path):
    with open(path) as my_data:
        data = json.load(my_data)
        return data


@fixture(params=load_jsondata(my_jsonpath))
def my_testdata(request):
    test_data = request.param
    return test_data


@fixture(scope="session")
def chrome_browser():
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=ChromeService(f'''/home/amalchacko/chromedriver'''))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
