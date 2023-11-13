from django.shortcuts import render
from .forms import SignUpForm


def home(request): #veiw function takes request as an argument (http request information)
    return render(request, 'home.html')

def sign_up(request):
    form = SignUpForm() 
    return render(request, 'sign_up.html', {'form': form})