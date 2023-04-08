from HomeModule import views
from django.urls import path, include
from chat.views import sendmessage,getMessages
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('dump', views.dump, name='dump'),
    path('profile', views.profile, name='profile'),
    path('fav', views.fav, name='fav'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.handlelogout, name='logout'),
    path('sendmessage', sendmessage, name='sendmessage'),
    path('getMessages/<str:roomkey>',getMessages, name='getMessages'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
