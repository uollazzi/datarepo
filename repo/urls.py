from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'repo'
urlpatterns = [
    # ex: /repo/
    path('', views.index, name='index'),
    # api
    # url(r'^records/$', views.Records.as_view(), name="records"),
    # ex: /repo/5/
    path('<int:record_id>/', views.detail, name='detail'),
]
