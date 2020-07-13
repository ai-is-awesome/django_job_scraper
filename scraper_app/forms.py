from django import forms
from src.indeed_global_urls import countries



CHOICES = [tuple([country, country]) for country in countries]


class ScraperForm(forms.Form):

	query = forms.CharField(label = 'Enter the Job title', max_length = 50)
	city = forms.CharField(label = 'Enter the city', max_length = 30, required = False)
	country = forms.CharField(label = 'Enter the country', widget = forms.Select(choices = CHOICES, ))
	num_pages = forms.IntegerField(label = 'Enter the number of pages to be scraped')

