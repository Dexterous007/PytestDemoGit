import time
import pytest
# from selenium.webdriver.chrome import webdriver  # headless mode
from selenium import webdriver
from selenium.webdriver.common.by import By

# use for headless mode.
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")


class Test1:

    @pytest.mark.xfail      # output:- test_sum_001 XPASS  ... 1 xpassed
    def test_sum_001(self):  # items ---> Test Case
        a = 5  # Test Case name --->  always start with "test_"
        b = 15
        sums = a + b
        print(sums)

        if sums == 20:
            print("test_sum_001 is passed")
            assert True
        else:
            print("test_sum_001 is failed")
            assert False

    def test_mul_002(self):  # Intentionally we failed this Test Case to see an
        a = 5  # assertion error.
        b = 15
        mul = a * b
        print(mul)

        if mul == 75:
            print("test_mul_002 is passed")
            assert True
        else:
            print("test_mul_002 is failed")
            assert False

    def sums_003(self):  # It will not consider or run in the output because of name.
        a = 30           # Test Case name should be "test_sums_003".
        b = 65           # It will not consider as a Test Case
        sums = a + b
        print(sums)

        if sums == 95:
            print("sums is passed")
            assert True
        else:
            print("sums is failed")
            assert False

    def test_add_004(self):
        a = 30
        b = 65
        add = a + b
        print(add)

        if add == 95:
            print("test_add_004 is Passed")
            assert True
        else:
            print("test_add_004 is failed")
            assert False

    @pytest.mark.sanity    # collected 6 items / 4 deselected / 2 selected of sanity only.
    def test_google(self):
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(options=chrome_options)  ## headless mode
        driver.get("https://www.google.com/")
        driver.maximize_window()
        time.sleep(2)
        logo = driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        time.sleep(2)  # In output, it shows flag as True so assert will display Test Case as Passed.
        print(logo)    # but if we take flag as False then it will display Test Case as Failed.
        if logo == True:    # here we take 'True' as a flag if it's displayed
            driver.close()  # then show it is True else show False.
            assert True     # Test Case status ---> Pass
        else:
            driver.close()  # else show False.
            assert False  # Test Case status ---> fail
