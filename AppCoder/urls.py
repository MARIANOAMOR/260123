from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('reparaciones', views.reparaciones, name="Reparaciones"),
    #path('clientes', views.clientes, name="Clientes"),
    path('gestionDeClientes', views.clientes, name="Clientes"),
    path('gestionDeClientes', views.clientes, name="Clientes"),
    path('registrarCliente/', views.registrarCliente),
    path('proveedores', views.proveedores, name="Proveedores"),
    path('repuestos', views.repuestos, name="Repuestos"),
    path('buscar/', views.buscar),
    path('leerClientes', views.leerClientes, name = "LeerClientes"),
    path('eliminarCliente/<Cliente_nombre>/', views.eliminarCliente, name="EliminarCliente"),
    path('editarCliente/<Cliente_nombre>/', views.editarCliente, name="EditarCliente"),
    path('reparacion/list', views.ReparacionList.as_view(), name='List'),
    # login y registro
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil')

    #path('',views.inicio,name='inicio'),
    #--------------Mascota-----------------------
    #path('mascota',views.animal,name='mascota'),
    #path('formularioMascota',views.formularioMascota,name='formularioMascota'),
    #path('leerMascota',views.leerMascota,name='leerMascota'),
    #path('eliminarMascota/<mascota_nombre>/',views.eliminarMascota,name='eliminarMascota'),
    #path('editarMascota/<mascota_nombre>/',views.editarMascota,name='editarMascota'),
    #path('busquedaMascota',views.busquedaMascota,name='busquedaMascota'),
    #path('buscar/',views.buscar),
    #--------------Persona-----------------------
    #path('persona',views.persona,name='persona'),
    #path('formularioPersona',views.formularioPersona,name='formularioPersona'),
    #path('leerPersona',views.leerPersona,name='leerPersona'), 
    #path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    #path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),
    #--------------Vetirinario-----------------------
    #path('veterinario',views.veterinario,name='veterinario'),
    #path('formularioVeterinario',views.formularioVeterinario,name='formularioVeterinario'),
    #path('leerVeterinario',views.leerVeterinario,name='leerVeterinario'), 
    #path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    #path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),
    

]

