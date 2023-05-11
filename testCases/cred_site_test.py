import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCred:

    def test_site_1010(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.maximize_window()
        time.sleep(2)
        offers = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offers)
        page_title = driver.title  # with the help of Title you get to know that whether you have
        print(page_title)  # reached at that page or not.

        if page_title == "Credence":  # here we took 'True' that's why it shows us an assertion error.
            assert True
        else:
            assert False

        ## =================================== OR ==================================== ##

        """if driver.title == "Credence":
            assert True
        else:
            assert False"""

    # How to find the position of mobile number from call dropdown.

    def test_site_1020(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "img[src='/website/images/enquiry.png']").click()
        time.sleep(2)
        # print(driver.find_element(By.CSS_SELECTOR, "div[id='popupDIv'] a:nth-child(9)").text)
        # time.sleep(2)

#   Now I have to find its position ---> # +91 9091929355  --> find length and use for loop.
#         length = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
#         print(length)  # PASSED [100%]   length = 6
#
#         for r in range(1, length+1):
#             contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
#             # print(contact)  # Check properly output with this print and without.
#             if contact == "+91 9091929355":
#                 print(r)
#                 break
#                 assert True
#             else:
#                 print(r)
#                 # assert False

#   we change the logic of the code:

        length = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
        # print(length)                     # PASSED [100%]   length = 6
        list = []

        for r in range(1, length + 1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            # print(contact)  # Check properly output with this print and without.
            list.append(contact)

            if "+91 9091929355" in list:
                print(r)
                # assert True
            else:
                print(r)
                # assert False




