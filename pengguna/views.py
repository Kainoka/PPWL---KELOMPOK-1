from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def pengguna_list(request):
    pengguna = User.objects.all()
    context = {
        'pengguna': pengguna,
    }
    return render(request, 'halaman/pengguna_list.html', context)