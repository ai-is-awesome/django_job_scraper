from django.shortcuts import render
from .forms import ScraperForm
from src.job_scraper import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.



def index(request):
    form = ScraperForm
    context = {'form' : form}
    return render(request, 'scraper_app/index.html', context)




def scrape(request):
    if request.method == 'GET':
        form = ScraperForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            city = form.cleaned_data['city']
            num_pages = form.cleaned_data['num_pages']





    query_manager = IndeedQueryManager(query = query, city = city, num_pages = num_pages)
    scraper =  IndeedJobScraper(query_manager)
    job_details = scraper.get_job_details()

    response = HttpResponse(content_type = 'application/ms-excel')

    response['Content-Disposition'] = f'attachment; filename="{query}-Jobs.xls"'
    
    wb.save(response)
    return response



    
def scrape(request):
    if request.method == 'GET':
        form = ScraperForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            city = form.cleaned_data['city']
            num_pages = form.cleaned_data['num_pages']
            country = form.cleaned_data['country']

    # response = HttpResponse(content_type = 'application/ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="Jobs.xls"'

    # query_manager = IndeedQueryManager(query = query, city = city, num_pages = num_pages, country = country)
    # scraper =  IndeedJobScraper(query_manager)
    # scraper.save_to_excel(response)

    query_manager = IndeedQueryManager(query = query, city = city, num_pages = num_pages, country = country)
    scraper =  IndeedJobScraper(query_manager)

    details= scraper.get_job_details()

    return render(request, 'scraper_app/scrape.html', {'details' : details})

    

    








def download(request, path):
    file_path = os.path.join()













