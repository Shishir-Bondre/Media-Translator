
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    #path('transcript/',views.getTranscript,name='getTranscript'),

    path('input/',views.getInput, name='getInput'),
    path('output/',views.getOutput, name='getOutput'),
    # path('login/',views.getLoginDetails,name='getLoginDetails'),
    # path('register/',views.getRegisterDetails,name='getRegisterDetails'),
    # path('logout/',views.user_logout , name='index'),

]