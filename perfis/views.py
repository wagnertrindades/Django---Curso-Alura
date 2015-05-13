from django.shortcuts import render

# Create your views here.
def index(resquest):
	return render(resquest, 'index.html')