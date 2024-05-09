from .views import HomeView, Sa1ytView, Sa2ytView, Sa3ytView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('1-sayt/', Sa1ytView.as_view(), name="sa1yt-page"),
    path('2-sayt/', Sa2ytView.as_view(), name="sa2yt-page"),
    path('3-sayt/', Sa3ytView.as_view(), name="sa3yt-page"),

]
