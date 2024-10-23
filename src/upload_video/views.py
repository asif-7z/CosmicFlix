from django.shortcuts import redirect, render,get_object_or_404,HttpResponse
from .form import upload,RegisterModel,SeriesModel,LoginForm
from django.contrib.auth.decorators import login_required
from .models import video,Series_Name
from mylist.models import mylist
from django.utils import timezone
from watchhistory.models import Watch_History
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
import imdb
import os
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User



imdb = imdb.IMDb()
# Create your views here.


@login_required
def upload_video(request):

    template_name = "videoupload.html"
    form = upload(request.POST or None,request.FILES or None)
    s_form = SeriesModel(request.POST or None,request.FILES or None)
    if form.is_valid() & s_form.is_valid():
        Name = s_form.save()
        
        obj = video.objects.create(**form.cleaned_data,series = Name)
        list = Name.video_set.all()
        for i in list:
            print(i.title)
        # form.save()
        # s_form.save()
        # form = upload()
        # s_form = SeriesModel()
         
    context = {"file": form,"poster":s_form}
    return render(request,template_name,context)

def home(request):
    obj = Series_Name.objects.all()
    obj2 = Series_Name.objects.all()[:3]
    user = request.user
    if str(user) == 'AnonymousUser':
        hist = {}
        last_played = "no history"
    else:
        hist = Watch_History.objects.filter(user=request.user).order_by('-timestamp')[:1]
        if hist:
            for i in hist:
                last_played = i.video_name.slug
        else:
                last_played="no history"
   

    poster = {"poster1":{"p":obj[0].poster.url,"n":obj2[0].Name,"d":obj2[0].detail},
              "poster2":{"p":obj2[1].poster.url,"n":obj2[1].Name,"d":obj2[1].detail},
              "poster3":{"p":obj2[2].poster.url,"n":obj2[2].Name,"d":obj2[2].detail}}


    template_name = "home.html"
    context = {"poster":obj,"cars":poster,"hist":hist,"lst_p":last_played}
    return render(request,template_name,context)

def category(request,type):
    template_name = "category.html"
    cat = Series_Name.objects.filter(type=type)
    genre = Series_Name.objects.all()
    query = request.GET.get('q',None)
    all_genre = []
    for i in genre:
        all_genre.append(i.genre)

    def remove_duplicates_across_all(genres_list):
        genre_set = set()
        for genres in genres_list:
            genre_set.update([genre.strip().lower() for genre in genres.split(',') if genre.strip()])
        return sorted(genre_set)

    unique_genres = remove_duplicates_across_all(all_genre)

    v_list = Series_Name.objects.search(query=query)
    context = {"category":cat,'genre':unique_genres,'g_list':v_list,"type":type}
    return render(request,template_name,context)

@login_required
def detail(request,Name):
    obj = Series_Name.objects.filter(Name=Name)
    o2 = Series_Name.objects.get(Name__icontains=Name)
    o2.count_views += 1
    o2.save()
    try:
        u_list = mylist.objects.get(my_list=o2)
        response = "Added"
        if request.method == "POST":
            u_list.delete()
            return redirect('.')
        
    except:
        response="Add in Mylist"
        if request.method == "POST":
            lobj = mylist.objects.create(user=request.user,my_list=o2)
            return redirect('.')

    
    id = None
    # x = os.system('ping facebook.com')
    # if x == 0:
    #     im = imdb.search_movie(Name)
    #     id = im[0].movieID
    #     movie_or_series = imdb.get_movie(id)
    #     # rating,votes = movie_or_series.data['rating'],movie_or_series['votes']
    #     # print(rating)
    #     # print(movie_or_series.data)
    # else:
    #     pass
    url = ''
    for i in obj:
        j = i.video_set.all()[0]
        url = j.slug
    

    # obj2 = video.objects.filter(slug=slug)
    # # url = ''
    # list = ''
    # v = {}
    # for i in obj2:
    #     url = i.get_url()
    #     list = i.get_list()
    #     v = {"Name":i.series.Name,"poster":i.series.poster.url,
    #           
    # "detail":i.series.detail,"time":i.series.time_stamp,"type":i.series.type}
    template_name = "detail.html"
    context = {"detail":obj,"url":url,"linkid":id,"response":response,"rating":"0","votes":"0"}
    return render(request,template_name,context)

@login_required
def play(request,slug):
    template_name = "play.html"
    vsource = video.objects.get(slug=slug)
    vsource.view_count += 1
    vsource.save()
    time = timezone.now()
    series = vsource
    watch,created = Watch_History.objects.get_or_create(user=request.user,video_name=series)
    if not created:
        watch.timestamp = time
        watch.save()
    genre = vsource.series.genre
    genre = genre.split(',')
    rec = Series_Name.objects.filter(genre__icontains= genre[0]) | Series_Name.objects.filter(genre__icontains= genre[1])
    title = vsource.series.Name
    list = video.objects.filter(slug__icontains=title)
    movies = Series_Name.objects.order_by('-count_views')[:10]
    context_name  = {"play":vsource,"list":list,"rec":rec,'movies': movies}
    return render(request,template_name,context_name)



@login_required
def most_watched(request):
    movies = Series_Name.objects.order_by('-count_views')[:10] # Top 10 most watched    
    # for i in movies:
    #     videos = i.video_set.all()
    #     for j in videos:
    #         print(j.slug)

    return render(request, 'most_watched.html', {'movies': movies})

@login_required
def update_series_list(request,Name):
    template_name= "update.html"
    obj = get_object_or_404(Series_Name,Name=Name)
    form = SeriesModel(request.POST or None,request.FILES or None, instance=obj)
    u_form = upload(request.POST or None,request.FILES or None)
    if u_form.is_valid():
        C_obj = video.objects.create(**u_form.cleaned_data)
    context = {"Name":form,"update":u_form}
    return render(request,template_name,context)


def list_obj(request,slug):
    temp = "list.html"
    # obj = video.objects.filter(slug=slug).series.Name
    # print(obj)
    listEp = video.objects.filter(slug__icontains=slug)
    print(listEp)
    poster = listEp[0].series.poster.url
    context = {"list":listEp,"poster":poster}
    return render(request,temp,context)

@login_required
def edit(request,slug):
    temp_name = "edit.html"
    obj = get_object_or_404(video,slug=slug)
    form = upload(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {"edit":form}
    return render(request,temp_name,context)
@login_required
def delete(request,slug):
    temp_name = "delete.html"
    obj = get_object_or_404(video,slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {"delete":obj}
    return render(request,temp_name,context)


def register(request):
    tempname = "Register.html"
    form = RegisterModel(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        # user.is_staff = form.cleaned_data.get('is_staff', True)
        user.save()
        form.save()
        return redirect('/login/')
    context = {"Register":form}

    return render(request,tempname,context)

def login_view(request):
    print(request.user)
    if request.method == 'POST':
        form = LoginForm(request, request.POST)  # Use your custom form if you created one
        if form.is_valid():
            login(request, form.get_user())
            # Redirect the user to a success page or dashboard
            return redirect('/')
    else:
        form = LoginForm()  # Use your custom form if you created one
    return render(request, 'login.html', {'login': form})

def user_logout(request):
    logout(request)
    return redirect('login')

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')

@login_required
def delete_user(request):
    template_name = "delete_user.html"
    user = request.user
    userobj = User.objects.get(username=user)
    if request.method == 'POST':
        if userobj.is_superuser:
            return HttpResponse('<h1 style="color:red";>Superuser cannot be deleted</h1>')
        else:
            userobj.delete()
            home = '/'
            return HttpResponse(f'<h2 style="color: green";>Account deleted succesfull</h2><a href="{home}">home</a>')
    context = {"username":userobj}
    return render(request,template_name,context)    
    
@login_required    
def settings_view(request):
    template_name = "account_settings.html"
    user = request.user
    obj = User.objects.get(username=user)
    context = {"profile":obj}
    return render(request,template_name,context)

@login_required
def account_info_view(request):
    template_name = "account-info.html"
    user=request.user
    obj = User.objects.get(username=user)
    print(obj.date_joined)
    context = {"profile":obj}
    return render(request,template_name,context)


