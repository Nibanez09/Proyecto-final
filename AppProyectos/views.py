from django.shortcuts import render
from AppProyectos.models import *
from AppProyectos.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


#Inicio

def inicio(request):
    return render(request, 'AppProyectos/inicio.html')

def sobre(request):
    return render(request, 'AppProyectos/about.html')

#Registro de usuario y login

def registro(request):

    if request.method == "POST":

        miFormulario = UserCreationForm(request.POST) 

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]
            miFormulario.save()

            return render(request, "AppProyectos/inicio.html")

    else:

        miFormulario = UserCreationForm()

    return render(request, "AppProyectos/autenticacion/registro.html", {"formulario1":miFormulario})


def editarUsuario(request):
    
    usuario = request.user

    if request.method == "POST":
        
        form = FormularioEditar(request.POST)
        
        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppProyectos/inicio.html")
        
    else:
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            })
            
    return render(request, "AppProyectos/editarPerfil.html", {"formulario":form, "usuario":usuario})





def iniciar_sesion(request):

    if request.method == "POST":

        miFormulario = AuthenticationForm(request, data = request.POST) 

        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get("username")
            clave = miFormulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=clave) #verificación de datos de inicio

            if miUsuario:

                login(request,miUsuario)
                mensaje = f"Bienvenido {miUsuario}"

            return render(request, "AppProyectos/inicio.html", {"mensaje":mensaje})

        else:
            mensaje = f"Datos incorrectos, verificar"

            return render(request, "AppProyectos/inicio.html", {"mensaje":mensaje})

    else:

        miFormulario = AuthenticationForm()

    return render(request, "AppProyectos/autenticacion/login.html", {"formulario1":miFormulario})

#------------------CRUD de datos------------------------------

#Clientes

class ClienteLista(ListView):
    model = Cliente
    template_name = "AppProyectos/clientes/cliente_list.html"

class ClienteCrear(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "empresa", "profesion", "email"]
    success_url = "/AppProyectos/clientes/lista"
    template_name = "AppProyectos/clientes/cliente_form.html"

class ClienteBorrar(LoginRequiredMixin,DeleteView): 
    model = Cliente
    success_url = "/AppProyectos/clientes/lista"
    template_name = "AppProyectos/clientes/cliente_confirm_delete.html"

class ClienteEditar(LoginRequiredMixin,UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "empresa", "profesion", "email"]
    success_url = "/AppProyectos/clientes/lista"
    template_name = "AppProyectos/clientes/cliente_form.html"

#Proyectos

class ProyectoLista(ListView):
    model = Proyecto
    template_name = "AppProyectos/proyectos/proyecto_list.html"

class ProyectoCrear(LoginRequiredMixin, CreateView):
    model = Proyecto
    fields = ["codigo", "fecha_recibido", "plazo", "categoria"]
    success_url = "/AppProyectos/proyectos/lista"
    template_name = "AppProyectos/proyectos/proyecto_form.html"

class ProyectoBorrar(LoginRequiredMixin,DeleteView): 
    model = Proyecto
    success_url = "/AppProyectos/proyectos/lista"
    template_name = "AppProyectos/proyectos/proyecto_confirm_delete.html"

class ProyectoEditar(LoginRequiredMixin,UpdateView):
    model = Proyecto
    fields = ["codigo", "fecha_recibido", "plazo", "categoria"]
    success_url = "/AppProyectos/proyectos/lista"
    template_name = "AppProyectos/proyectos/proyecto_form.html"

#Responsables

class ResponsableLista(ListView):
    model = Responsable
    template_name = "AppProyectos/responsables/responsable_list.html"

class ResponsableCrear(LoginRequiredMixin, CreateView):
    model = Responsable
    fields = ["nombre", "apellido"]
    success_url = "/AppProyectos/responsables/lista"
    template_name = "AppProyectos/responsables/responsable_form.html"

class ResponsableBorrar(LoginRequiredMixin,DeleteView): 
    model = Responsable
    success_url = "/AppProyectos/responsables/lista"
    template_name = "AppProyectos/responsables/responsable_confirm_delete.html"

class ResponsableEditar(LoginRequiredMixin,UpdateView):
    model = Responsable
    fields = ["nombre", "apellido"]
    success_url = "/AppProyectos/responsables/lista"
    template_name = "AppProyectos/responsables/responsable_form.html"


#Búsqueda y resultados

def buscarProyecto(request):
    return render(request, 'AppProyectos/buscarProyecto.html')

def resultados(request):

    if request.method == "GET":

        categoriaBusqueda = request.GET['categoria']
        resultadosProyectos = Proyecto.objects.filter(categoria__icontains=categoriaBusqueda)
    
        return render(request, 'AppProyectos/resultados.html', {'d1':categoriaBusqueda, 'd2':resultadosProyectos})

    return render(request, 'AppProyectos/resultados.html')

