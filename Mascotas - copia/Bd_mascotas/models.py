from django.db import models
from django.utils.timezone import  now

tipo_mascota=[
    ["Perro", "Perro"],
    ["Gato", "Gato"],
    ["Ave", "Ave"],
    ["Reptil", "Reptil"],
    ["Roedores", "Roedores"],
    ["Conejo", "Conejo"],
]

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    tipo_masco = models.CharField(max_length=45, choices=tipo_mascota)
    raza_masco = models.CharField(max_length=45)
    nomb_masco = models.CharField(max_length=45)
    naci_masco = models.DateField()
    foto_masco = models.ImageField(upload_to='mascotas/')
    id_persona3 = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona3')

    class Meta:
        managed = False
        db_table = 'mascota'


class MascotaServicio(models.Model):
    id_mascota_servicio = models.AutoField(primary_key=True)
    id_servicio1 = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio1')
    id_mascota1 = models.ForeignKey(Mascota, models.DO_NOTHING, db_column='id_mascota1')
    fech_servi_masco = models.DateField()

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id_mascota1)


    class Meta:
        managed = False
        db_table = 'mascota_servicio'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nomb_produ = models.CharField(max_length=45)
    desc_produ = models.CharField(max_length=60)
    prec_produ = models.FloatField()
    foto_produ = models.ImageField(upload_to='productos/')

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoUsuario(models.Model):
    id_producto_usuario = models.AutoField(primary_key=True)
    id_persona2 = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_persona2')
    id_producto2 = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto2')
    cant_producto = models.IntegerField(blank=True, null=True)
    total_producto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_usuario'


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nomb_serv = models.CharField(max_length=45)
    desc_serv = models.CharField(max_length=1000)
    prec_serv = models.FloatField()
    imag_serv = models.ImageField(upload_to='servicios/')

    class Meta:
        managed = False
        db_table = 'servicio'


roles_usuarios=[
    [0, "Administrador"],
    [1, "Cliente"]
]

class Usuario(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    usua_usuar = models.CharField(unique=True, max_length=45, blank=True, null=True)
    cont_usuar = models.CharField(max_length=45, blank=True, null=True)
    nomb_usuar = models.CharField(max_length=45, blank=True, null=True)
    apel_usuar = models.CharField(max_length=45, blank=True, null=True)
    dire_usuar = models.CharField(max_length=45, blank=True, null=True)
    tele_usuar = models.CharField(max_length=45, blank=True, null=True)
    corr_usuar = models.CharField(max_length=45, blank=True, null=True)
    tipo_usuar = models.IntegerField(blank=True, null=True, choices=roles_usuarios)
    foto_usuar = models.ImageField(upload_to='usuarios/')

    class Meta:
        managed = False
        db_table = 'usuario'
        

class  Categoria(models.Model):
    nomb_categ=models.CharField(max_length=100, verbose_name="Nombre")
    crea_categ=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name='categoria'
        
    def __str__(self):
        texto="{0}"
        return texto.format(self.nomb_categ)
    

class Post(models.Model):
    titu_post=models.CharField(max_length=200, verbose_name="Título")
    cont_post=models.TextField(verbose_name="Contenido")
    fech_post=models.DateTimeField(default=now,verbose_name="Fecha de publicación")
    foto_post=models.ImageField(upload_to="BlogImg",null=True,blank=True,verbose_name="Imagen")
    id_persona =models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True)
    categorias=models.ManyToManyField(Categoria, verbose_name="Categorias")
    Fcreacion=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    Fedicion=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name='post'
        
    def __str__(self):
        texto="{0}"
        return texto.format(self.titu_post)