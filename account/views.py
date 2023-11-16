from django.shortcuts import render
from .models import Carousel, CarouselCat, UserProfile
from .forms import UserRegistrationForm
# Create your views here.
#Static Page
def index(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="Home")
    return render(request, 'account/home.html', {'slides':slides})

def about(request):
    slides = Carousel.objects.filter(pubblicato=True, categoria__nome="About")
    return render(request,'account/about.html', {'slides':slides})

#Registrazione Utente
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Creo un nuovo oggetto utente ma non lo salvo
            new_user = user_form.save(commit=False)
            #Setto la password
            new_user.set_password(user_form.cleaned_data['password']) #Django codifica la password in SHA256
            #Ora posso salvare in nuovo utente
            new_user.save()
            #Dopo aver salvato il nuvo utente posso prendere l'id a creare una nuova riga nella tabella profilo con l'id utente appena creato
            #UserProfile.objects.create(user=new_user) #Non serve perchè fatto in model con receiver
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html', {'user_form':user_form})