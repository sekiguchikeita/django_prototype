from django.shortcuts import render
from .models import Board
from django.http import HttpResponse


# Create your views here.
def home(request):
#    return HttpResponse('aaaaa')
    boards = Board.objects.order_by
    return render(request, 'app/home.htm',{'boards':boards})