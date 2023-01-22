from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from tutotradeproject import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str 
from . tokens import generate_token
from .forms import OglosznieForm, CustomUserCreationForm, NauczajOglosznieForm, ThreadForm, MessageForm 
from .models import *
from .filters import OgloszenieFilter, NauczajOgloszenieFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import F,Q
from django.template import loader


# Create your views here.
def glowna(request):
    ogloszenia = Ogloszenie.objects.all()

    myfilter = OgloszenieFilter(request.GET, queryset=ogloszenia)
    
    ogloszenia = myfilter.qs

    return render(request, "strona/index.html", {'ogloszenia':ogloszenia, 'myfilter':myfilter})

def nauczaj(request):
    nogloszenia = NauczajOgloszenie.objects.all()

    myfilter = NauczajOgloszenieFilter(request.GET, queryset=nogloszenia)
    
    nogloszenia = myfilter.qs

    return render(request, "strona/nauczajinnych.html", {'nogloszenia':nogloszenia, 'myfilter':myfilter})
def rejestracja(request):
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():
            email = form.cleaned_data.get('email')
            messages.success(request, 'Twoje konto zostało pomyślnie utworzone')
            form.save()
            return redirect('logowanie')
        else:
            if User.objects.filter(username=username):
                messages.error(request, "Nazwa użytkownika jest zajęta. Spróbuj użyć innej.")
            if User.objects.filter(email=email):
                messages.error(request, "Ten email został już wykorzystany.")
            elif password1 != password2:
                messages.error(request, "Podane hasła różnią się od siebie.")
            elif len(password1)<8:
                messages.error(request, "Hasło jest za krótkie.")
            else:
                messages.error(request, "Hasło nie zawiera znaku specjalnego, cyfry i wielkiej litery")

 
    context = {'form':form}
    return render(request, "strona/rejestracja.html", context)

def logowanie(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request ,username=username,password=password)

        if user is not None:
            login(request, user)
            
            return redirect('stronaglowna')
        else: 
            messages.error(request, "Błędne dane!")
            return redirect('logowanie')


    return render(request, "strona/logowanie.html")

def wyloguj(request):
    logout(request)
    messages.success(request, "Zostałes pomyślnie wylogowany.")
    return redirect('logowanie')
    
def activate(request, uidb64, token):
    try:
        uid  = force_str(urlsafe_base64_encode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('stronaglowna')
    else:
        return render(request,'activation_failed.html')

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        użytkownik = User.objects.get(pk=pk)
        ogloszenia = Ogloszenie.objects.filter(author = użytkownik)
        nogloszenia = NauczajOgloszenie.objects.filter(author = użytkownik)

        context = {
            'użytkownik':użytkownik,
            'ogloszenia':ogloszenia,
            'nogloszenia':nogloszenia,
            }
        return render(request, "strona/użytkownik.html", context)


@login_required(login_url='logowanie')
def tworzenieOgloszenia(request):
    form = OglosznieForm()
    if request.method == "POST":
        form = OglosznieForm(request.POST)
        OglosznieForm.użytkownik = User.username
        if form.is_valid():
            nowe_ogloszenie = form.save(commit=False)
            nowe_ogloszenie.author = request.user
            nowe_ogloszenie.save()
            return redirect('stronaglowna')

    context = {'form':form}
    return render(request, 'strona/tworzenie_ogloszenia.html', context)

@login_required(login_url='logowanie')
def nauczajTworzenieOgloszenia(request):
    form = NauczajOglosznieForm()
    if request.method == "POST":
        form = NauczajOglosznieForm(request.POST)
        OglosznieForm.użytkownik = User.username
        if form.is_valid():
            nowe_ogloszenie = form.save(commit=False)
            nowe_ogloszenie.author = request.user
            nowe_ogloszenie.save()
            return redirect('nauczajinnych')

    context = {'form':form}
    return render(request, 'strona/tworzenie_ogloszenia_nauczaj.html', context)

@login_required(login_url='logowanie')
def chat(request):
    return render(request, "strona/chat.html")

class ListThreads(View):
  def get(self, request, *args, **kwargs):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    context = {
        'threads': threads
    }
    return render(request, 'strona/chat.html', context)
    
class CreateThread(View):
    @login_required(login_url='logowanie')
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        context = {
        'form': form
        }
        return render(request, 'strona/create_thread.html', context)

    @login_required(login_url='logowanie')
    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')
        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            
            if form.is_valid():
                sender_thread = ThreadModel(
                user=request.user,
                receiver=receiver
                )
                sender_thread.save()
                thread_pk = sender_thread.pk
                return redirect('thread', pk=thread_pk)
        except:
            return redirect('create-thread')

class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
        'thread': thread,
        'form': form,
        'message_list': message_list
        }
        return render(request, 'strona/thread.html', context)

class CreateMessage(View):

    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
        )
        message.save()
        return redirect('thread', pk=pk)

def deleteOrder(request, pk):
    ogloszenia = Ogloszenie.objects.get(id=pk)
    if request.method == "POST":
        ogloszenia.delete()
        return redirect('użytkownik', request.user.pk)
    context={'item':ogloszenia,}
    return render(request, 'strona/delete.html', context )

def braktresci(request):
    return render(request, 'strona/braktresci.html')