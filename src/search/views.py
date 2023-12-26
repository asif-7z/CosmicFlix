from django.shortcuts import render
from .models import search
from upload_video.models import video,Series_Name

# Create your views here.

def searchquery(request):
    template_name = "view.html"
    query = request.GET.get('q',None)
    user = None
    v_list = None
    if request.user.is_authenticated:
        user=request.user
        if query is not None:
            search.objects.create(user=user,query=query)
            v_list = Series_Name.objects.search(query=query)
    context = {"query": query,"search":v_list}
    return render(request,template_name,context)