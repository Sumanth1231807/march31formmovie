from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global moviename,yor,dir,dis,producer,driver
    moviename= input("Enter the movie name :")
    yor=input("Year of release :")
    dir=input("Director Name :")
    dis=input("Distributor :")
    producer=input("Producer name :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(10)
    driver.close()

def test_movie(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yor)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(dir)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(dis)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[1]").click()
    driver.find_element_by_name("subbtn").click()
    time.sleep(2)