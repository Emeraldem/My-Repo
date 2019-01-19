from django.urls import re_path
from . import views

urlpatterns = {
    re_path(r'^$', views.showall),
    re_path(r'all/', views.hello),
    re_path(r'get/(?P<video_id>\d+)/$', views.showone)
}
