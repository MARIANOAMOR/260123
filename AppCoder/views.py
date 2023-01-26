from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from AppCoder.models import Reparacion, Cliente
from AppCoder.forms import ReparacionFormulario, ClienteFormulario, UserRegisterForm, UserEditForm

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def registrarCliente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    email = request.POST['txtEmail']         
    direccion = request.POST['txtDireccion']
    observaciones = request.POST['txtObservaciones']

    cliente = Cliente.objects.create(codigo =codigo, nombre=nombre, apellido=apellido, telefono=telefono, email=email, direccion=direccion, observaciones=observaciones)
    messages.success(request, '¡Cliente registrado!')
    return redirect('/AppCoder/gestionDeClientes')

def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()
    messages.success(request, '¡Cliente eliminado!')
    return redirect('/AppCoder/gestionDeClientes')
    #return redirect('/')

def reparacion(request):

      reparacion =  Reparacion(nombre="Desarrollo web", camada="19881")
      reparacion.save()
      documentoDeTexto = f"--->Reparacion: {reparacion.nombre}   Camada: {reparacion.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def proveedores(request):

      return render(request, "AppCoder/proveedores.html")


def repuestos(request):

      return render(request, "AppCoder/repuestos.html")


def reparaciones(request):

      if request.method == 'POST':

            miFormulario = ReparacionFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  reparacion = Reparacion (nombre=informacion['reparacion'], camada=informacion['camada']) 

                  reparacion.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ReparacionFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/reparaciones.html", {"miFormulario":miFormulario})




def clientes(request):
      #if request.method == 'POST':
      #      miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html
      #      print(miFormulario)
      #      if miFormulario.is_valid:   #Si pasó la validación de Django
      #            informacion = miFormulario.cleaned_data
      #            cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'],telefono=informacion['telefono'],
      #             email=informacion['email'], direccion=informacion['direccion'], observaciones=informacion['observaciones']) 
      #            cliente.save()
      #            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #else: 
      #      miFormulario= ClienteFormulario() #Formulario vacio para construir el html
      #return render(request, "AppCoder/clientes.html", {"miFormulario":miFormulario})
      #return render(request, "AppCoder/gestionDeClientes.html", {"miFormulario":miFormulario})

      #aca lo que hago es a penas ingresa en el template gestion de clientes, listar todos los clientes que estan en la base de datos
      cliente=Cliente.objects.all()
      return render(request, "AppCoder/gestionDeClientes.html", {"cliente":cliente})






def buscar(request):

      if  request.GET["camada"]:
	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            reparaciones = Reparacion.objects.filter(camada__icontains=camada)
            return render(request, "AppCoder/inicio.html", {"reparaciones":reparaciones, "camada":camada})
      else: 
	      respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)


def leerClientes(request):
      clientes = Cliente.objects.all() #trae todos los clientes
      contexto= {"clientes":clientes} 
      return render(request, "AppCoder/leerClientes.html",contexto)

def eliminarCliente(request, cliente_nombre):

    cliente = Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()
    # vuelvo al menú
    clientes = Cliente.objects.all()  # trae todos los clientes
    contexto = {"clientes": clientes}
    return render(request, "AppCoder/leerClientes.html", contexto)

def editarCliente(request, cliente_nombre):
    # Recibe el nombre del Cliente que vamos a modificar
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.telefono = informacion['telefono']
            cliente.email = informacion['email']
            cliente.direccion = informacion['direccion']
            cliente.observaciones = informacion['observaciones']
            cliente.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ClienteFormulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido,
                                                   'telefono': cliente.telefono, 'email': cliente.email,
                                                   'direccion': cliente.direccion, 'observaciones': cliente.observaciones})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarCliente.html", {"miFormulario": miFormulario, "cliente_nombre": cliente_nombre})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ReparacionList(ListView):

    model = Reparacion
    template_name = "AppCoder/reparaciones_list.html"

class ReparacionDetalle(DetailView):

    model = Reparacion
    template_name = "AppCoder/reparacion_detalle.html"

class ReparacionCreacion(CreateView):

    model = Reparacion
    success_url = "/AppCoder/reparacion/list"
    fields = ['nombre', 'camada']

class ReparacionUpdate(UpdateView):

    model = Reparacion
    success_url = "/AppCoder/reparacion/list"
    fields = ['nombre', 'camada']

class ReparacionDelete(DeleteView):

    model = Reparacion
    success_url = "/AppCoder/reparacion/list"


# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})


def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
