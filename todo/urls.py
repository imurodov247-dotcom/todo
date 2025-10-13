from django.urls import path
from . import views




urlpatterns = [
    path('',views.index),
    path("salom/",views.salom),
    path("hayr/",views.hayr)

]