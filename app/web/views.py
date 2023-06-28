from django.shortcuts import render
from modelCore.models import QAPost

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def process_price(request):
    data = "傳到html的資料"
    return render(request,'web/process_price.html',{'data':data})

def types(request):
    style = request.GET.get('style')

    if style == None:
        style = 'all'

    return render(request,'web/types.html',{'style':style})

def featured_case(request):
    return render(request,'web/featured_case.html')

def q_and_a(request):
    posts = QAPost.objects.all().order_by('id')
    return render(request,'web/q_and_a.html',{'posts':posts})

def contact(request):
    return render(request,'web/contact.html')