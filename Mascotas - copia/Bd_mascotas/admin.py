from django.contrib import admin
from .models import Producto, Usuario, Mascota, Servicio, MascotaServicio, ProductoUsuario, Categoria, Post 

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nomb_produ","desc_produ", "prec_produ","foto_produ")
admin.site.register(Producto, ProductoAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_persona", "usua_usuar","cont_usuar", "nomb_usuar","apel_usuar", "dire_usuar", "tele_usuar", "corr_usuar", "tipo_usuar")
admin.site.register(Usuario, UsuarioAdmin)

class MascotaAdmin(admin.ModelAdmin):
    list_display = ("tipo_masco", "raza_masco","nomb_masco", "naci_masco","foto_masco", "id_persona3")
admin.site.register(Mascota, MascotaAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nomb_serv", "desc_serv","prec_serv", "imag_serv")
admin.site.register(Servicio, ServicioAdmin)

class MascotaServicioAdmin(admin.ModelAdmin):
    list_display = ("id_servicio1", "id_mascota1","fech_servi_masco")
admin.site.register(MascotaServicio, MascotaServicioAdmin)

class ProductoUsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_persona2", "id_producto2","cant_producto", "total_producto")
admin.site.register(ProductoUsuario , ProductoUsuarioAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display=("titu_post","cont_post","fech_post","foto_post","Fcreacion","Fedicion")
    ordering=('titu_post','fech_post')
    list_filter=('id_persona_id__nomb_usuar','titu_post')
admin.site.register(Post,BlogAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nomb_categ","crea_categ")
admin.site.register(Categoria,CategoriaAdmin)