from django.shortcuts import render
from .forms import ScraperForm
# Create your views here.



def index(request):
	form = ScraperForm
	context = {'form' : form}
	return render(request, 'scraper_app/index.html', context)




def scrape(request):
	if request.method == 'GET':
		form_data = ScraperForm(request.GET)


	context = {'form_data' : form_data}

	return render(request, 'scraper_app/scrape.html', context)
