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

def genre(request):
    template_name = "genre.html"
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

    print(unique_genres)
    v_list = Series_Name.objects.search(query=query)
    context = {'genre':unique_genres,'g_list':v_list,"q_type":query}
    return render(request,template_name,context)
