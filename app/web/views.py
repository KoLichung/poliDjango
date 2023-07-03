from django.shortcuts import redirect,render
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
    if request.method == 'POST':
        userName = request.POST.get('customerName')
        email = request.POST.get('customerEmail')
        phone = request.POST.get('customerPhone')
        line = request.POST.get('customerLine')
        subject = request.POST.get('customerSubject')
        message = "name:"+userName + "\n" + "email:"+email + "\n" + "phone:"+phone + "\n" + "line:"+line + "\n" + "subject:"+subject + "\n"
        from mailapp.tasks import send_test_mail
        send_test_mail('網站新案件:'+userName, message)
        return redirect('message_sent')


    return render(request,'web/contact.html')