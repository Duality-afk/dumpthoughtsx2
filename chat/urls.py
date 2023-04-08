from chat import views
from django.urls import path, include

urlpatterns = [
    path('/<str:postkey>/', views.room, name='home'),
    

]

