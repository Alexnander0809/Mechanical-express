from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .models import Usuario

#region principal

def principal(request):
    return render(request, "Home/principal.html")

def solicitar_servicio(request):
    return render(request, "Home/solicitar_servicio.html")

def reserva(request):
    return render(request, "Home/reserva.html")

def contactenos(request):
    return render(request, "Home/contactenos.html")

#endregion

#region usuario


def verificarusuario(request):
    if request.method == 'POST':
        if request.POST.get("email") and request.POST.get("contraseña"):
            usuario = Usuario()
            usuario.email = request.POST.get('email')
            usuario.contraseña = request.POST.get('contraseña')
            verificar = connection.cursor()
            verificar.execute("call verificarusuario('"+usuario.email+"','"+usuario.contraseña+"')")
            return redirect("/productos/listado")
        else:
            return render()
    else:
        return render(request, 'login.html')



def insertarusuario(request):
    if request.method=="POST":
        if 'form1' in request.POST:
            rol = request.POST.get("rol")
            nombres = request.POST.get("nombres")
            apellidos = request.POST.get("apellidos")
            direccion = request.POST.get("direccion")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            contraseña = request.POST.get("contraseña")

            print("Valores recibidos:")
            print("Rol:", rol)
            print("Nombres:", nombres)
            print("Apellidos:", apellidos)
            print("Dirección:", direccion)
            print("Teléfono:", telefono)
            print("Email:", email)
            print("Contraseña:", contraseña)

            if rol and nombres and apellidos and direccion and telefono and email and contraseña:
                usuario = Usuario()
                usuario.rol = rol
                usuario.nombres = nombres
                usuario.apellidos = apellidos
                usuario.direccion = direccion
                usuario.telefono = telefono
                usuario.email = email
                usuario.contraseña = contraseña
                usuario.save()
                print("Usuario guardado exitosamente")
                return redirect("/")
            else:   
                mensaje = "Algunos campos requeridos no están presentes en el formulario."
                print(mensaje)
                return render(request, 'Login/insertar.html', {'mensaje': mensaje})
        elif 'form2' in request.POST:
            if request.POST.get("email") and request.POST.get("contraseña"):
                name = request.POST.get("email")
                pasdfs = request.POST.get("contraseña")
                print(name + " " + pasdfs)
                user = Usuario.objects.filter(email=name)
                if user.exists():
                    mensaje = "bien"
                    print(mensaje)
                    return render(request, 'Login/insertar.html', {'mensaje': mensaje})
            else: 
                mensaje = "Algunos campos requeridos no están presentes en el formulario."
                print(mensaje)
                return render(request, 'Login/insertar.html', {'mensaje': mensaje})
        else: 
            mensaje = "No has hecho nada"
            print(mensaje)
            return render(request, 'Login/insertar.html', {'mensaje': mensaje})
    else:
        return render(request, 'Login/insertar.html')

    
# def listadousuario(request):
#     usuario = Usuario.objects.all()
#     return render(request, "Login/listado.html", {'usuario': usuario})

# def actualizarusuario(request, idusuario):
#     if request.method=="POST":
#         if request.POST.get("rol") and request.POST.get("nombre") and request.POST.get("apellido") and request.POST.get("telefono") and request.POST.get("email") and request.POST.get("contraseña") and request.POST.get("edad"):
#             usuario = Usuario.objects.get(id=idusuario)
#             usuario.cedula = request.POST.get("cedula")
#             usuario.apellido = request.POST.get("apellido")
#             usuario.telefono = request.POST.get("telefono")
#             usuario.email = request.POST.get("email")
#             usuario.contraseña = request.POST.get("contraseña")
#             usuario.edad = request.POST.get("edad")
#             usuario.save() 
#             return redirect("/usuario/listado")
#     else:
#         usuario = Usuario.objects.filter(id=idusuario)
#         return render(request, 'Login/actualizar.html', {'usuario':usuario})
    
# def borrarusuario(request, idusuario):
#     usuario = Usuario.objects.get(id=idusuario)
#     usuario.delete()
#     return redirect("/Login/listado")


#endregion