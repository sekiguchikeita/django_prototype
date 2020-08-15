from django.shortcuts import render
from .models import Board
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bs4 import BeautifulSoup
import requests


# Create your views here.
def home(request):
#    return HttpResponse('aaaaa')
    boards = Board.objects.order_by
    return render(request, 'app/home.htm',{'boards':boards})

@login_required
def create(request):
    # return HttpResponse('aaaaa')  
    return render(request, 'app/create.htm')

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

def index(request):

    url = request.GET.get('url')

    if url == None:
        d = {
             'category' : "urlを入力して下さい。"
        }
    else:
        # 入力されたURLでの本文を取得する。
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        doc = soup.find_all('p')

        #取得した本文を形態素解析し、名詞のみ抽出
        word_list=''
        for text in doc:
            m = MeCab.Tagger()
            m_text = m.parse(text.text)
            for row in m_text.split("\n"):
                word =row.split("\t")[0]#タブ区切りになっている１つ目を取り出す。ここには形態素が格納されている
                if word == "EOS":
                    break
                else:
                    pos = row.split("\t")[1]#タブ区切りになっている2つ目を取り出す。ここには品詞が格納されている
                    slice = pos[:2]
                    if slice == "名詞":
                        word_list = word_list +" "+ word

        d = {
            'category': word_list
        }

    return render(request, 'app/create.htm',d)