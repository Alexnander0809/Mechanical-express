from django import forms
from django.shortcuts import redirect, render
from mechanical_express.models import Roles, Usuario

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
def insertarusuario(request):
    if request.method=="POST":
        if request.POST.get("rol_ida") and request.POST.get("nombres") and request.POST.get("apellidos") and request.POST.get("telefono") and request.POST.get("email") and request.POST.get("contraseña"):
            usuario = Usuario()
            usuario.rol_ida = request.POST.get("rol_ida")
            usuario.nombres = request.POST.get("nombres")
            usuario.apellidos = request.POST.get("apellidos")
            usuario.telefono = request.POST.get("telefono")
            usuario.email = request.POST.get("email")
            usuario.contraseña = request.POST.get("contraseña")
            usuario.save() 
            return redirect("/Login/listado")
    else:
        return render(request, 'Login/insertar.html')
    
def listadousuario(request):
    usuario = Usuario.objects.all()
    return render(request, "Login/listado.html", {'usuario': usuario})

def actualizarusuario(request, idusuario):
    if request.method=="POST":
        if request.POST.get("rol") and request.POST.get("nombre") and request.POST.get("apellido") and request.POST.get("telefono") and request.POST.get("email") and request.POST.get("contraseña") and request.POST.get("edad"):
            usuario = Usuario.objects.get(id=idusuario)
            roles = Roles()
            roles.rol = request.POST.get("rol")
            usuario.cedula = request.POST.get("cedula")
            usuario.apellido = request.POST.get("apellido")
            usuario.telefono = request.POST.get("telefono")
            usuario.email = request.POST.get("email")
            usuario.contraseña = request.POST.get("contraseña")
            usuario.edad = request.POST.get("edad")
            usuario.save() 
            return redirect("/usuario/listado")
    else:
        usuario = Usuario.objects.filter(id=idusuario)
        return render(request, 'Login/actualizar.html', {'usuario':usuario})
    
def borrarusuario(request, idusuario):
    usuario = Usuario.objects.get(id=idusuario)
    usuario.delete()
    return redirect("/Login/listado")

# def validarusuario():

def validarcorreo(self):
    email = self.cleaned_data.get('email')
    if Usuario.objects.filter(email=email).exists():
        raise forms.ValidationError(u'El email ya está registrado, prueba con otro')
    return email

#endregion