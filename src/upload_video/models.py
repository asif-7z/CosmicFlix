from django.db import models
from django.conf import settings
from django.db.models import Q


User = settings.AUTH_USER_MODEL
# Create your models here.

# class VideoQuerySet(models.QuerySet):
    
#     def search(self,query):
#         lookup=Q(Q(title__icontains=query)|
#                  Q(content__icontains=query)|
#                  Q(slug__icontains=query)|
#                  Q(series__genre__icontains=query)|
#                  Q(series__Name__icontains=query)|
#                  Q(series__detail__icontains=query)|
#                  Q(series__type__icontains=query)|
#                  Q(user__username__icontains=query)
#                  )
#         return self.filter(lookup)

# class VideoManager(models.Manager):
#     def get_queryset(self):
#         return VideoQuerySet(self.model, using=self._db)
    
#     def search(self, query=None):
#         if query is None:
#             return self.get_queryset().none()
#         return self.get_queryset().search(query)

class Series_NameQuerySet(models.QuerySet):
    
    def search(self,query):
        lookup=Q(Q(Name__icontains=query)|
                 Q(detail__icontains=query)|
                 Q(genre__icontains=query)|
                 Q(type__icontains=query)
                 )
        return self.filter(lookup)

class Series_nameManager(models.Manager):
    def get_queryset(self):
        return Series_NameQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)



class Series_Name(models.Model):
    Name = models.CharField(max_length=200,null=True)
    poster = models.ImageField(upload_to='images/',null=True)
    genre = models.CharField(max_length=30,null=True)
    type = models.CharField(null=False,max_length=10)
    detail = models.TextField(null=True,max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True)
    count_views = models.IntegerField(default=0,null=True)

    objects = Series_nameManager()

    def detail_url(self):
        return f"{self.Name}/detail"
    
    class Meta:
        ordering = ['-time_stamp']
    
    def __str__(self):
        return self.Name
    
    
    


class video(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,)
    series = models.ForeignKey(Series_Name,on_delete=models.SET_NULL,null=True)
    title = models.CharField(null=False,max_length=200)
    slug = models.SlugField(unique=False)
    file = models.FileField(upload_to='video/',null=False)
    image = models.ImageField(upload_to='images/',null=False)
    content = models.TextField(null=False)
    view_count = models.IntegerField(default=0,null=True)

    # objects = VideoManager()

    def get_url(self):
        return f"/play/{self.slug}"
    
    def get_list(self):
        return f"{self.slug}/episodes"
    
    def edit_url(self):
        return f"{self.get_url()}/edit"
    
    def delete_url(self):
        return f"{self.get_url()}/delete"
    
    def upload_url():
        return "/upload/"

    def __str__(self):
        return self.title+' - '+self.series.Name
    

