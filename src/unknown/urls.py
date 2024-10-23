"""
URL configuration for unknown project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from search.views import searchquery,genre
from mylist.views import my_list_view
from watchhistory.views import watch_history_view
from django.conf.urls.static import static
from django.conf import settings
from upload_video.views import (upload_video,play,list_obj,edit,delete,
                                register,home,update_series_list,detail,
                                category,login_view,user_logout,ChangePasswordView,delete_user,
                                settings_view,account_info_view,most_watched
                                
                                )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('category/<str:type>/',category),
    path('mylist/',my_list_view),
    path('history/',watch_history_view),
    path('upload/',upload_video),
    path('<str:slug>/detail/episodes/',list_obj),
    path('play/<str:slug>/edit/',edit),
    path('play/<str:slug>/delete/',delete),
    path('play/<str:slug>/',play),
    path('most_watched/',most_watched),
    path('<str:Name>/detail/',detail),
    path('<str:Name>/update/',update_series_list),
    path('search/',searchquery),
    path('genre/',genre),
    path('Register/',register),
    path('login/',login_view,name='login'),
    path('logout/',user_logout,name='logout'),
    path('settings/',settings_view),
    path('settings/account-info/',account_info_view),
    path('settings/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('settings/delete_user/',delete_user),
    path('api/',include('upload_video.api.urls'))
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
