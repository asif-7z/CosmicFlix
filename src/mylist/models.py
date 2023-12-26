from django.db import models
from upload_video.models import Series_Name
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class mylist(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    my_list = models.ForeignKey(Series_Name,null=True,on_delete=models.SET_NULL)
    time_stamp = models.DateTimeField(auto_now_add=True)