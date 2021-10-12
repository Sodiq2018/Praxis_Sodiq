from django.db import models
from django.shortcuts import render, redirect
from . import models
# Create your views here.

def readMakanan(req):
    if req.POST:
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.makanan.objects.create(jenis = input_jenis, nama= input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(req, "makanan/index.html", {
        "data": data,
    })

def readMinuman(req):
    if req.POST:
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama= input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(req, "minuman/index.html", {
        "data": data,
    })

def readPesanan(req):
    if req.POST:
        get_makanan = req.POST["makanan"]
        get_minuman = req.POST["minuman"]
        get_jumlah_makanan = req.POST["jumlah_makanan"]
        get_jumlah_minuman = req.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman, jumlah_makanan=get_jumlah_makanan, jumlah_minuman=get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render (req, "pesanan/index.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })


def hapus(request, id):
    models.makanan.objects.filter(id= id).delete()
    return redirect('/')