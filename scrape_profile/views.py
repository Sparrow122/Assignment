from rest_framework.views import APIView
from django.http import JsonResponse


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time 
from .serializers import MyDataSerializer
import re


# Create your views here.

class Scrape_View(APIView):

    #Scraping data using selenium
    @staticmethod
    def scrape_url(profile_url):
        browser = webdriver.Chrome()
        browser.get(profile_url)
        time.sleep(3)
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section[aria-labelledby="public_profile_contextual-sign-in-modal-header"]')))
        popup = browser.find_element(By.CSS_SELECTOR, 'section[aria-labelledby="public_profile_contextual-sign-in-modal-header"] > button svg')
        popup.click()
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, 300);")
        Soup_obj = BeautifulSoup(browser.page_source, 'html.parser')
        name_ele = Soup_obj.select('h1[class*="top-card-layout__title"]')[0]
        headline_ele = Soup_obj.select('h2[class*="top-card-layout__headline"]')
        if headline_ele:
            headline = headline_ele[0].get_text().strip().replace(r'\n','')
        else:
            headline = ''
        about_ele = Soup_obj.select('section[data-section="summary"] p')[0]
        experiences_ele = Soup_obj.select('section[data-section="experience"] li')
        educations_ele = Soup_obj.select('section[data-section="educationsDetails"] li')
        browser.quit()
        name = name_ele.get_text().strip().replace(r'\n','')
        about = about_ele.get_text().strip().replace(r'\n','')
        education = []
        for elem in educations_ele:
            education.append({"institute": elem.select('h3')[0].get_text().strip().replace(r'\n',''),
                              "course": elem.select('h4')[0].get_text().strip().replace(r'\n','')})
        experiences = []
        for elen in experiences_ele:
            experiences.append({"designation": elen.select('h3')[0].get_text().strip().replace(r'\n',''),
                                "company": elen.select('h4')[0].get_text().strip().replace(r'\n','')})
        data = {
            "name": name,
            "about": about,
            "headline": headline,
            "education": education,
            "experience": experiences
        }

        #send data to serializer
        serial = MyDataSerializer(data)
        serialized_data = serial.data
        return serialized_data
    

    def post(self, request):
        profile_url = request.data.get('profile_url', None)
        if (not profile_url):  #if profile's url is not sent with data in endpoint request.
            return JsonResponse({"Message": "Profile url not provied!"})
        else:
            scraped_data = Scrape_View.scrape_url(profile_url)   
            return JsonResponse({"data": scraped_data})