from django.shortcuts import render
from .models import Producto, Servicio, Post
from .forms import BlogForms
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

def index(request): #pagina de inicio
    return render(request, 'index.html')

def contact(request): #pagina de contacto
    return render(request, 'contact.html')

def about(request): 
    return render(request, 'about.html')

def products(request): 
    
    productos = Producto.objects.all()
    return render(request, 'products.html', {'productos': productos})

def service(request): #Galeria
    
    servicios = Servicio.objects.all()
    
    return render(request, 'service.html', {'servicios': servicios})

class BlogListView(ListView):
    model = Post
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class BlogCreate(CreateView):
    model = Post 
    form_class = BlogForms
    template_name = 'Bd_mascotas/CreateBlog.html'
    success_url = reverse_lazy('ListarPost')
    
    

def registration(request): #Registro de nuevos usuarios
    
    return render(request, 'registration.html')

def single(request, id): #blog
    
    post = Post.objects.filter(id=id)
    
    return render(request, 'single.html', {'post': post})

def blog(request):
    
    blogPost = Post.objects.all()
    return render(request, 'blog.html', {'posts': blogPost})


