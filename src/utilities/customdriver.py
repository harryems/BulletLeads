from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import contextlib
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui    
from bs4 import BeautifulSoup
import re

class CustomDriver(object):
    def __init__(self):
        pass
    def getInfo(self,driver):
        wait = ui.WebDriverWait(driver,10)
        
        medidas=driver.find_element_by_class_name("color_swatch_current_text").text
        areasImpresion=[]
        tabs=driver.find_element_by_class_name("cc-tabs").find_elements_by_class_name("cc-tab")
        for tab in tabs:
            if tab.text=="Decorating Options":
                tab.click()
        driver.implicitly_wait(1)
        wait.until(lambda driver: driver.find_element_by_id('decoratingMethods'))
        
#         decodetails= driver.find_element_by_class_name("deco-details")
#         print driver.find_element_by_class_name("methodDetailsDiv_1400-43BK_8").text
#         print   decodetails.find_element_by_xpath("//div[@class='methodDetailsDiv_1400-43BK_8']").text

        html = driver.page_source
        
        soup =  BeautifulSoup(html, "html.parser")
        details=soup.find("div",{"class":"wp-product-details-tab"})
        description= details.find("p").text
#         for node in soup.findAll(attrs={'class': re.compile(r"methodDetailsDiv_v*")}):
#             if node.h3:
# #                 print node
#                 areasImpresion.append({"name":node.h3.text,"description":node.find("p").text.encode("utf-8")})
                
        return description,medidas,areasImpresion
#                 print node.h3.text
#                 print node.find("p").text

#         for method in decodetails.find_elements_by_tag_name("div"):
#             if "methodDetailsDiv_" in method.get_attribute("class"):
#                 #print method.get_attribute('innerHTML')
#                 #print "********************************"
#                 #try:
#                 print method.find_element_by_class_name("no-top").getText()
#                 print method.findElement(By.CSS_SELECTOR("p")).getText()
                #except:
                #    continue
        
        