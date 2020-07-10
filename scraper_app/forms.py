from django import forms



class ScraperForm(forms.Form):

	query = forms.CharField(label = 'Enter the Job title', max_length = 50)
	city = forms.CharField(label = 'Enter the city', max_length = 30)
	num_pages = forms.IntegerField(label = 'Enter the number of pages to be scraped')
