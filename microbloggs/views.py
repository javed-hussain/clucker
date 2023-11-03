from django.shortcuts import render


def home(request): #veiw function takes request as an argument (http request information)
    return render(request, 'home.html')