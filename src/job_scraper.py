import requests
from bs4 import BeautifulSoup
import time
import xlwt
from xlwt import Workbook
from src.indeed_global_urls import countries_to_urls
from src.indeed_query_manager import IndeedQueryManager
from src.requests_module import Request
from src.io_operations import IOOperations


class IndeedJobScraper(Request):
    origin_url = 'https://www.indeed.in'
    #query = IndeedQueryManager(query = '', city = '', country = 'India', num_pages = 1)


    def __init__(self, query):
        '''
        Input: IndeedQueryManager object


        Constructs the query. 

        '''
        self.query = query

    def get_text_or_tag(self, tag):
        if tag == None:
            return None
        else:
            return tag.text
    

    def get_soup(self, url = None):
        
        resp = self.get(url)
        text = resp.text
        soup = BeautifulSoup(text, 'lxml')
        return soup



    def get_details_from_job_container(self, soup):
        '''
        input: A job container containing all the text of a single Job box in indeed(beatufiul soup object)
        output: Dictionary with details of the Job
        '''
        
        results = {}
        title = soup.find('h2' , class_ = 'title')
        results['title'] = title.a.get('title')
        
        results['company'] = self.get_text_or_tag(soup.find('span', class_ = 'company'))
        
        results['location'] = (soup.find('div', class_ = 'recJobLoc').get('data-rc-loc'))
        
        results['salary'] = self.get_text_or_tag(soup.find('span', class_ = 'salaryText'))
        
        results['description'] = self.get_text_or_tag(soup.find('div', class_ = 'summary'))
        
        return results
        


    def get_job_details(self,):
        urls_list = self.query.get_urls_from_query()
        jobs_list = []
        card_class = 'jobsearch-SerpJobCard'
        for url in urls_list:
            soup = self.get_soup(url)
            for job_detail in soup.find_all('div', class_ = card_class):
                jobs_list.append(self.get_details_from_job_container(job_detail))

                #Adding sleep
                time.sleep(0.5)

        return jobs_list            


    def save_to_excel(self, path = None):

        json = self.get_job_details()
        instance = IOOperations(json)
        data = instance.json_to_list()
        instance.add_rows(data)
        instance.save(path)



    def query_formatter(query):
        return query.replace(' ', '+')







