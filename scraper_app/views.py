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

    response['Content-Disposition'] = 'attachment; filename="Jobs.xls"'


    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
    
    
    
    

    wb.save(response)
    return response



    
def scrape(request):
    if request.method == 'GET':
        form = ScraperForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            city = form.cleaned_data['city']
            num_pages = form.cleaned_data['num_pages']




    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Jobs.xls"'

    query_manager = IndeedQueryManager(query = query, city = city, num_pages = num_pages)
    scraper =  IndeedJobScraper(query_manager)
    scraper.save_to_excel(response)
    return response

    

    








def download(request, path):
    file_path = os.path.join()













