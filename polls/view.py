from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.loader import get_template
def index(request):
	template = get_template('index.html')
	variables = Context({
		'head_title': 'asssss',
		'page_title': '123456',
		'page_body': 'harshitttt'
	})
	output = template.render(variables)
	return HttpResponse(output)
