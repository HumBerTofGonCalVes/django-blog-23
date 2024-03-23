from blogapi.views import index
from django.urls import path

app_name = 'blogapi'

urlpatterns = [
    # blogapi:index
    path('', index, name='index'),
]
