from django.db import models
from django.conf import settings
from upload_video.models import Series_Name


User = settings.AUTH_USER_MODEL

# Create your models here.
class Watch_History(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    video_name = models.ForeignKey(Series_Name,null=True,on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(null=True,auto_now_add=True)