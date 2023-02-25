from django.urls import path
from AppProyectos.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Start"),
    path('about/', sobre, name="About"),


    #Registro e ingreso usuario

    path("cuentas/registro/", registro, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("cuentas/logout/", LogoutView.as_view(template_name="AppProyectos/autenticacion/logout.html"), name="Logout"),
    path("cuentas/editar/", editarUsuario, name="EditarUsuario"),

    #Clientes

    path("clientes/lista", ClienteLista.as_view(), name="Ver Clientes"),
    path("clientes/nuevo", ClienteCrear.as_view(), name="Crear Clientes"),
    path("clientes/borrar/<int:pk>", ClienteBorrar.as_view(), name="Borrar Clientes"),
    path("clientes/editar/<int:pk>", ClienteEditar.as_view(), name="Editar Clientes"),

    #Proyectos

    path("proyectos/lista", ProyectoLista.as_view(), name="Ver Proyectos"),
    path("proyectos/nuevo", ProyectoCrear.as_view(), name="Crear Proyectos"),
    path("proyectos/borrar/<int:pk>", ProyectoBorrar.as_view(), name="Borrar Proyectos"),
    path("proyectos/editar/<int:pk>", ProyectoEditar.as_view(), name="Editar Proyectos"),

    #Responsables

    path("responsables/lista", ResponsableLista.as_view(), name="Ver Responsables"),
    path("responsables/nuevo", ResponsableCrear.as_view(), name="Crear Responsables"),
    path("responsables/borrar/<int:pk>", ResponsableBorrar.as_view(), name="Borrar Responsables"),
    path("responsables/editar/<int:pk>", ResponsableEditar.as_view(), name="Editar Responsables"),   

    
    #Búsqueda
    path("buscarProyecto/", buscarProyecto),
    path("resultados_busqueda/", resultados),
]
