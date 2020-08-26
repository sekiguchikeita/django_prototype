from django.shortcuts import render
from .models import Board
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests
#スクレイピング
from .models import News
from django.views.generic import CreateView
from django.urls import reverse_lazy
from urllib.request import Request, urlopen   
import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
#    return HttpResponse('aaaaa')
    boards = Board.objects.order_by
    return render(request, 'app/home.html',{'boards':boards})

@login_required
def create(request):
    # return HttpResponse('aaaaa')  
    return render(request, 'app/create.html')

    # if request.method == 'POST':
    #     if request.POST['title'] and request.POST['comment'] and request.POST['url'] and request.FILES['image']:
    #         app = app()
    #         app.title = request.POST['title']
    #         app.comment = request.POST['comment']
    #         if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
    #             product.url = request.POST['url']
    #         else:
    #             app.url = 'http://' + request.POST['url']
    #         app.image = request.FILES['image']
    #         app.pub_date = timezone.datetime.now()
    #         app.hunter = request.user
    #         app.save()
    #         return redirect('/app/' + str(app.id))
    #     else:
    #         return render(request,'app/create.htm')
    # else:
    #     return render(request, 'app/create.htm')

# def send_request(request):
#     print('****************')
#     print('ajax is done')
#     return HttpResponse("ajax is done!")

#Views.py

#スクレイピング

class Create(CreateView):
   template_name = 'create.html'
   model = News
   fields = ('url',)
   success_url = reverse_lazy('list')
   


# urlのHTMLを取得
def listfunc(request):
    for post in News.objects.all():
        url = post.url
        print("aaa" + url)
        list = []
  
    # for post in News.objects.all():
    # url = request
    # print("aaa" + url)
    # print(request)
    # list = []

    response = requests.get(url)
    html = urllib.request.urlopen(url)
# htmlをBeautifulSoupでパース
    soup = BeautifulSoup(html, "html.parser")
# タイトル要素の文字列を取得
    # soup_title = str(soup.title) 
    
    head_info = soup.find('head')

    meta_img = head_info.find('meta', {'property' : 'og:image'})
    soup_img = meta_img['content']

    meta_description = head_info.find('meta', {'name' : 'description'})
    soup_desc = meta_description['content']

    soup_title = head_info.find('title').getText()

    print(soup_title)
    list.append([soup_title, soup_desc, soup_img])
    # list.clear()
    
    context = {'list':list}
  
    # return render(request, 'list.html',context1)
    return render(request, 'create.html',context)