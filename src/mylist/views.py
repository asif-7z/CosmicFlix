from django.shortcuts import render
from .models import mylist
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def my_list_view(request):
    template_name = "mylist.html"
    m = mylist.objects.filter(user=request.user)
    context_name = {"ml":m}
    return render(request,template_name,context_name)