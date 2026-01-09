from django.db import models

class Obat(models.Model):
    nama_obat = models.CharField(max_length=100)
    jenis_obat = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.IntegerField()
    tanggal_kadaluarsa = models.DateField()

    def __str__(self):
        return self.nama_obat
