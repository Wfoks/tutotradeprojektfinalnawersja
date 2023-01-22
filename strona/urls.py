from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .views import ListThreads, CreateThread, ThreadView, CreateMessage, ProfileView




urlpatterns = [
    path('', views.glowna, name="stronaglowna"),
    path('nauczajinnych', views.nauczaj, name="nauczajinnych"),
    path('rejestracja', views.rejestracja, name="rejestracja"),
    path('logowanie', views.logowanie, name="logowanie"),
    path('wyloguj', views.wyloguj, name="wyloguj"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('użytkownik/<str:pk>/', ProfileView.as_view(), name="użytkownik"),
    path('tworzenie_ogloszenia', views.tworzenieOgloszenia, name="tworzenie_ogloszenia"),
    path('nauczaj_tworzenie_ogloszenia', views.nauczajTworzenieOgloszenia, name="nauczaj_tworzenie_ogloszenia"),
    path('chat', ListThreads.as_view(), name="chat"),
    path('chat/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('chat/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-mesage', CreateMessage.as_view(), name="create-message"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('braktresci', views.braktresci, name='braktresci')
]
