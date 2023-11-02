from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("Hello World!")

def greeting_view(request):
    username = request.GET.get('username')
    context = {'username': username}
    return render(request, 'greeting.html', context)

def list_view(request):
    products = ['apples', 'bananas', 'carrots', 'dates']
    return HttpResponse("This should list products!")