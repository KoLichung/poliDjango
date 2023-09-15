from django.shortcuts import redirect,render
from modelCore.models import QAPost

def index(request):
    context = {
       "page_title":"首頁",
       "description":"波麗壁布居家輕裝潢，快速又大器！防霉，固色，好清潔。",
     }
    return render(request,'web/index.html',context)

def about(request):
    context = {
       "page_title":"關於我們",
       "description":"為了應對台灣長年潮濕的氣候環境，我們經過上百款布料的嚴格測試，確保波麗壁布以100%純布織造，能夠經得起時間的考驗。",
     }
    return render(request,'web/about.html',context)

def process_price(request):
    context = {
       "page_title":"服務流程與報價",
       "description":"波麗服務過上百位滿意客戶，相比壁紙，波麗壁布不會在3到5年後硬化或剝落，讓您省卻更換的困擾。立即觀看服務流程與報價！",
     }
    return render(request,'web/process_price.html',context)

def types(request):
    style = request.GET.get('style')

    if style == None:
        style = 'all'

    context = {
       "style":style,
       "page_title":"款式選擇",
       "description":"我們有上百款是提供選擇，亦可根據款式修改顏色，滿足您量身訂造的渴望！",
     }

    return render(request,'web/types.html',context)

def featured_case(request):
    context = {
       "page_title":"精選案例",
       "description":"我們以100%滿意的服務為目標，服務的對象廣泛，小家庭裝修，餐廳，公司等，請看我們的精選案例！",
     }
    return render(request,'web/featured_case.html',context)

def q_and_a(request):
    posts = QAPost.objects.all().order_by('id')
    context = {
       "posts":posts,
       "page_title":"常見問與答",
       "description":"問與答收集了我們常見的問題，提供您解決方案，若不清楚的部分，隨時點擊右下角聯繫客服！",
     }
    return render(request,'web/q_and_a.html',context)

def contact(request):
    context = {
       "page_title":"聯絡我們",
       "description":"任何合作方案或諮詢，立即聯絡我們。",
     }

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


    return render(request,'web/contact.html',context)

def message_sent(request):
    return render(request,'web/message_sent.html')