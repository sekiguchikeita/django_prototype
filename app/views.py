from django.shortcuts import render
from .models import Board
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
#    return HttpResponse('aaaaa')
    boards = Board.objects.order_by
    return render(request, 'app/home.htm',{'boards':boards})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['comment'] and request.POST['url'] and request.FILES['image']:
            app = app()
            app.title = request.POST['title']
            app.comment = request.POST['comment']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                app.url = 'http://' + request.POST['url']
            app.image = request.FILES['image']
            app.pub_date = timezone.datetime.now()
            app.hunter = request.user
            app.save()
            return redirect('/app/' + str(app.id))
        else:
            return render(request,'app/create.htm')
    else:
        return render(request, 'app/create.htm')