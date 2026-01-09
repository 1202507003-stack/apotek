from django.shortcuts import render, redirect, get_object_or_404
from .models import Obat

def index(request):
    data = Obat.objects.all()
    return render(request, 'obat/index.html', {'data': data})

def tambah(request):
    if request.method == 'POST':

        Obat.objects.create(
            nama_obat=request.POST['nama_obat'],
            jenis_obat=request.POST['jenis_obat'],
            stok=request.POST['stok'],
            harga=request.POST['harga'],
            tanggal_kadaluarsa=request.POST['tanggal_kadaluarsa']
        )
        return redirect('index')
    return render(request, 'obat/tambah.html')

def edit(request, id):
    obat = get_object_or_404(Obat, id=id)
    if request.method == 'POST':
        obat.nama_obat = request.POST['nama_obat']
        obat.jenis_obat = request.POST['jenis_obat']
        obat.stok = request.POST['stok']
        obat.harga = request.POST['harga']
        obat.tanggal_kadaluarsa = request.POST['tanggal_kadaluarsa']
        obat.save()
        return redirect('index')
    return render(request, 'obat/edit.html', {'obat': obat})

def hapus(request, id):
    obat = get_object_or_404(Obat, id=id)
    obat.delete()
    return redirect('index')
