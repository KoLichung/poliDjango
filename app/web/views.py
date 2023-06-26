from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'web/index.html')

def about(request):
    return render(request,'web/about.html')

def process_price(request):
    data = "傳到html的資料"
    return render(request,'web/process_price.html',{'data':data})

def types(request):
    style = request.GET.get('style')
    return render(request,'web/types.html',{'style':style})

def featured_case(request):
    return render(request,'web/featured_case.html')

def q_and_a(request):
    return render(request,'web/q_and_a.html')

def contact(request):
    return render(request,'web/contact.html')