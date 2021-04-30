# Creación de grupos con código 
import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','videojuegos.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from usuarios.models import Usuario

grupo_administradores = Group.objects.create(name='administrador')
grupo_usuarios = Group.objects.create(name='usuarios')

content_type = ContentType.objects.get_for_model(Usuario)

permiso_usuarios = Permission.objects.create(
    codename = 'permiso_usuario',
    name = 'Permiso requerido para el grupo usuarios',
    content_type = content_type
)

permiso_administradores = Permission.objects.create(
    codename = 'permiso_administradores',
    name = 'Permiso requerido para el grupo administradores',
    content_type = content_type
)

grupo_usuarios.permissions.add(permiso_usuarios)
grupo_administradores.permissions.add(permiso_administradores)

administrador = Usuario.objects.create_user('38192811@uaz.edu.mx',password='juca123')
administrador.groups.add(grupo_administradores)

# Usuario.objects.create_superuser('admin@uaz.edu.mx',password='soyeladmin')

# {% if perms.myapp.permission %} 