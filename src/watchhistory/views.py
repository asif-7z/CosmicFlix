from django.shortcuts import render
from .models import Watch_History
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
# Create your views here.
def watch_history_view(request):
    template_name = "history.html"
    obj = Watch_History.objects.filter(user=request.user).order_by('-timestamp')
    for i in obj:
        print(i.video_name)
    if request.method == "POST":
        obj.delete()
    context = {"history":obj}
    return render(request,template_name,context)
