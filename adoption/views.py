from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from django.http import Http404


# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import User1
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
	pets = Pet.objects.all()
	return render(request, 'home.html', {'pets': pets})
# 	will use render instead
#	return HttpResponse('<p> home view</p>')

def pet_detail(request, id):
	try:
		pet = Pet.objects.get(id=id)
	except Pet.DoesNotExist:
		raise Http404('Pet not Found')
	return render(request, 'pet_detail.html', {'pet': pet})

def welcome(request):
	pets = Pet.objects.all()
	return render(request, 'welcome.html', {'pets': pets})

def profile(request):
	users = User1.objects.all()
	return render(request, 'profile.html', {'users': users})
# 	will use render instead
#	return HttpResponse('<p> home view</p>')