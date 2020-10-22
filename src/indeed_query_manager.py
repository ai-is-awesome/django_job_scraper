from src.indeed_global_urls import countries_to_urls


class IndeedQueryManager:
    #origin_url = 'https://www.indeed.in/'
   

    def __init__(self, query = '', city = '', country = 'India', num_pages = 1):
        self.query = query
        self.country = country
        self.city = city
        self.num_pages = num_pages
        self.origin_url = countries_to_urls[self.country]



    def get_urls_from_query(self):
        start = 0
        urls = list()

        for i in range(self.num_pages):
            url = self.origin_url + f'jobs?q={self.query}&start={start}&l={self.city}'
            #url = f'https://www.indeed.co.in/jobs?q={self.query}&start={start}&l={self.city}'
            urls.append(url)
            start += 10

        return urls
    
    def set_query(self, query):
        self.query= query

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_num_pages(self, num_pages):
        self.num_pages = num_pages

