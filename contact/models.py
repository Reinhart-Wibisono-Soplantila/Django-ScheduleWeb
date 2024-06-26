from django.db import models
from .validators import validate_NamaLengkap

# Create your models here.
class contactModel(models.Model):
    NamaLengkap=models.CharField(
        max_length=20,
        validators=[validate_NamaLengkap]
        )
    
    
    gender = (
        ("P", 'Pria'),
        ('W', 'Wanita'),
    )
    Jenis_Kelamin = models.CharField(
        max_length=1,
        choices=gender,
        default='P'
    )
    
    # tanggal_lahir = models.DateField()
    
    Email = models.EmailField()
    
    Alamat = models.TextField()
    
    # Agree = models.BooleanField()
    
    # Kode_Pos = models.IntegerField()
    # Kota = models.CharField(max_length=100)
    # Provinsi = models.CharField(max_length=100)
    Publised = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}. {}".format(self.id, self.NamaLengkap)