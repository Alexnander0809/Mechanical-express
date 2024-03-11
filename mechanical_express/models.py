from django.db import models

class Afiliados(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    fecha_nacimiento = models.CharField(max_length=250)
    telefono = models.CharField(max_length=11)
    correo = models.CharField(max_length=250)
    sede = models.CharField(max_length=250)
    taller_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "afiliados"

class Calificaciones(models.Model):
    comentario = models.CharField(max_length=250)
    puntuacion = models.CharField(max_length=250)
    fecha = models.CharField(max_length=250)
    taller_ida = models.CharField(max_length=11)
    usuario_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "calificaciones"

class Historial_reservas(models.Model):
    reserva_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "historial_reservas"

class Reserva(models.Model):
    direccion = models.CharField(max_length=200)
    estado_reserva = models.CharField(max_length=200)
    fecha_creacion = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    fecha_cita = models.CharField(max_length=250)
    usuario_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "reserva"  

class Roles(models.Model):
    tipo_rol = models.CharField(max_length=100)
    class Meta:
        db_table = "roles"  

class Sedes(models.Model):
    nombre_sede = models.CharField(max_length=250)
    ubicacion = models.CharField(max_length=250)
    taller_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "sedes"  

class Servicios(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.CharField(max_length=10)
    tiempo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500)
    taller_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "servicios"  

class Taller(models.Model):
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=11)
    descripcion = models.CharField(max_length=250)
    numero_reservas = models.CharField(max_length=11)
    horario_taller = models.CharField(max_length=100)
    class Meta:
        db_table = "taller"  

class Usuario(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=12)
    fecha_creacion = models.CharField(max_length=250)
    rol_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "usuario"   

class Usuario_taller(models.Model):
    usuario_ida = models.CharField(max_length=11)
    taller_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "usuario_taller" 

class Vehiculos(models.Model):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=100)
    año_fabricacion = models.CharField(max_length=11)
    fecha_registro = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    usuario_ida = models.CharField(max_length=11)
    class Meta:
        db_table = "vehiculos"
