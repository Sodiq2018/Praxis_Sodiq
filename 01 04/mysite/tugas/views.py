from django.db import models
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from. import models



def index(request):
    if request.POST:

        data = request.POST['nama']
        #print(data)

        models.tugas.objects.create(nama = request.POST ['nama'])

    hasil1 = models.tugas.objects.all()
    return render(request, 'index.html', {'isi' : hasil1})

def about(request):
    return HttpResponse("Halaman About")
    
