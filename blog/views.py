from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Projekt
def index(request):
    #posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    projekty = Projekt.objects.all()[0:3]
    return render(request, 'blog/index.html',{'projekty':projekty})
def view_projekt(request,id):
    projekt = Projekt.objects.get(pk=id)
    return render(request,'blog/projekt.html',{'projekt_view':projekt})
def o_mnie(request):
    return render(request,'blog/omnie.html',{})
    
# Create your views here.
