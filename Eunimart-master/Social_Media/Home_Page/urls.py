from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('login_signup',views.login_signup),
    path('register',views.register),
    path('dashboard',views.dashboard),
    path('tweet',views.tweet),
    path('delete_tweet/<int:delete_id>/',views.delete_tweet),
]
