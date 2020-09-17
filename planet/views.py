from django.shortcuts import render
# Create your views here.
import time
from django.views.decorators.cache import cache_page

cache_page(60*15)
def index(request):
    time.sleep(5)
    return render(request,"index.html")