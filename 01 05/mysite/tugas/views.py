from django.db import models
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, request
from. import models



def index(request):
    if request.POST:

        data = request.POST['nama']
        print(data)

        models.tugas.objects.create(nama = request.POST ['nama'])

    hasil1 = models.tugas.objects.all()
    return render(request, 'index.html', {'isi' : hasil1})

def hapus(request, id):
    models.tugas.objects.filter(id= id).delete()
    return redirect('/')

def detail (request, id):
    data = models.tugas.objects.filter(id= id).first()
    print(data)
    return render(request, "detail.html", {
        "detailData": data,
    })

def edit(request, id):
    if request.POST:
        input = request.POST['nama']
        print(input)
        models.tugas.objects.filter(id= id).update(nama = input)
        return redirect('/')

    data = models.tugas.objects.filter(id = id).first()
    return render(request, "edit.html", {
        "detailData" : data,
    })    
