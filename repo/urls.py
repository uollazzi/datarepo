from django.urls import path

from . import views

app_name = 'repo'
urlpatterns = [
    # ex: /repo/
    path('', views.index, name='index'),
    # ex: /repo/5/
    path('<int:record_id>/', views.detail, name='detail'),
]