
import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from blog.models import Post, Categoria
from servicios.models import Servicio
from .forms import *
from datetime import datetime
from .permissions import *
from django.contrib.auth.models import Permission


#Trabajando con usuarios
@view_user_permission
def user(request):
    users = User.objects.all()
    return render(request, "usuarios/usuarios.html", {"users": users})

@edit_user_permission
def edit_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)  # Si tienes un formulario de edición, pásale los datos y la instancia del usuario
        if form.is_valid():
            form.save()
            return redirect('administrador:usuarios')  # Redirige a la vista de lista de usuarios o a donde quieras
    else:
        form = UserEditForm(instance=user)  # Si es una solicitud GET, crea una instancia del formulario con los datos actuales del usuario
    
    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'user': user})

@delete_user_permission
def delete_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('administrador:usuarios')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'usuarios/eliminar_usuario.html', {'user': user})

@add_user_permission
def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.last_login = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            user.save()
            return redirect('administrador:usuarios')
    else:
        form = UserAddForm()

    template = 'usuarios/agregar_usuario.html'
    return render(request, template, {'form': form})



#Trabajando con roles
@view_rol_permission
def rol(request):

    # Obtener una lista de usuarios con sus permisos
    users_with_permissions = User.objects.prefetch_related('user_permissions').all()

    context = {
        'users_with_permissions': users_with_permissions
    }

    return render(request, 'roles/usuarios_roles.html', context)

def rolUser(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Obtener el usuario o mostrar 404 si no existe

    # Obtener los permisos del usuario
    user_permissions = user.user_permissions.all()

    context = {
        'selected_user': user,
        'user_permissions': user_permissions
    }

    return render(request, 'roles/usuario_permisos.html', context)

@delete_rol_permission
def delete_rolUser(request, user_id, permission_id):

    user = User.objects.get(pk=user_id)
    permission = Permission.objects.get(pk=permission_id)

    if request.method == 'POST':
        user.user_permissions.remove(permission)
        return redirect('administrador:roles')
        
    return render(request, 'roles/delete_usuarioPermiso.html', {'user': user, 'permission': permission})

@add_rol_permission
def add_rolUser(request, user_id):
    
    user = get_object_or_404(User, pk=user_id)
    
    all_permissions = Permission.objects.all()
    missing_permissions = all_permissions.exclude(id__in=user.user_permissions.values_list('id', flat=True))

    context = {
        'user': user,
        'missing_permissions': missing_permissions,
    }

    return render(request, 'roles/add_usuarioPermiso.html', context)

def agregarRol(request, user_id, permission_id):

    user = get_object_or_404(User, pk=user_id)
    permission = get_object_or_404(Permission, pk=permission_id)

    # Agrega la relación de permiso al usuario
    user.user_permissions.add(permission)

    context = {
        'selected_user': user,
        'selected_permission':permission,
    }

    return redirect('administrador:roles')



#Trabajando con blogs
@view_post_permission
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogs/blog.html', {'posts': posts})

@edit_post_permission
def edit_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = BlogEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('administrador:blogs')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = BlogEditForm(instance=post)

    return render(request, 'blogs/editar_post.html', {'form': form, 'post': post})

@delete_post_permission
def delete_blog(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('administrador:blogs')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'blogs/eliminar_post.html', {'post': post})

@add_post_permission
def add_blog(request):
    if request.method == 'POST':
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            post = form.save(commit=False)
            post.fecha_publicacion = datetime.now()
            post.save()
            return redirect('administrador:blogs')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = BlogAddForm()

    template = 'blogs/agregar_post.html'
    return render(request, template, {'form': form})



#Trabajando con Categorias blogs
@view_categoria_permission
def blogsCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, "blogsCategorias/categorias.html", {"categorias": categorias})

@add_categoria_permission
def add_blogCategoria(request):
    if request.method == 'POST':
        form = BlogCategoriaAddForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            categoria.save()
            return redirect('administrador:blogsCategorias')
    else:
        form = BlogCategoriaAddForm()

    template = 'blogsCategorias/agregar_categoria.html'
    return render(request, template, {'form': form})

""" def delete_blogCategoria(request, postCategoria_id):
    categoria = get_object_or_404(Post, id=postCategoria_id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('administrador:blogsCategorias')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'blogsCategorias/eliminar_categoria.html', {'categoria': categoria}) """

@edit_categoria_permission
def edit_blogCategoria(request, postCategoria_id):
    categoria = get_object_or_404(Categoria, id=postCategoria_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = BlogCategoriaEditForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('administrador:blogsCategorias')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = BlogCategoriaEditForm(instance=categoria)

    return render(request, 'blogsCategorias/editar_categoria.html', {'form': form, 'categoria': categoria})



#Trabajando con servicios
@view_servicio_permission
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicio/servicios.html", {"servicios": servicios})

@add_servicio_permission
def add_servicios(request):
    if request.method == 'POST':
        form = ServicioAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            servicio = form.save(commit=False)
            servicio.fecha_publicacion = datetime.now()
            servicio.save()
            return redirect('administrador:servicios')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = ServicioAddForm()

    template = 'servicio/agregar_servicio.html'
    return render(request, template, {'form': form})

@edit_servicio_permission
def edit_servicios(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ServicioEditForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('administrador:servicios')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ServicioEditForm(instance=servicio)

    return render(request, 'servicio/editar_servicio.html', {'form': form, 'servicio': servicio})

@delete_servicio_permission
def delete_servicios(request, servicio_id):
   
    servicio = get_object_or_404(Servicio, id=servicio_id)
    
    if request.method == 'POST':
        servicio.delete()
        return redirect('administrador:servicios')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'servicio/eliminar_servicio.html', {'servicio': servicio})



#Trabajando con productos
@view_producto_permission
def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/productos.html", {"productos": productos})

@add_producto_permission
def add_productos(request):
    if request.method == 'POST':
        form = ProductoAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Agrega estas líneas para verificar la imagen que se está recibiendo
            print(request.FILES)  # Deberías ver la información de la imagen en la consola
            producto = form.save(commit=False)
            producto.fecha_publicacion = datetime.now()
            producto.save()
            return redirect('administrador:productos')
        else:
            print(form.errors)  # Esto te mostrará los errores de validación si los hay
    else:
        form = ProductoAddForm()

    template = 'productos/agregar_producto.html'
    return render(request, template, {'form': form})

@edit_producto_permission
def edit_productos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ProductoEditForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administrador:productos')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ProductoEditForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

@delete_producto_permission
def delete_productos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('administrador:productos')  # Redirige a la vista de lista de usuarios o a donde quieras
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})



#Trabajando con Categoria productos
@view_categoriaProd_permission
def categotiasProd(request):
    categoriasProd = CategoriaProd.objects.all()
    return render(request, "productosCategorias/categorias.html", {"categoriasProd": categoriasProd})

@add_categoriaProd_permission
def add_categoriasProd(request):
    if request.method == 'POST':
        form = ProductoCategoriaAddForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.fecha_publicacion = datetime.now()  # Asigna la fecha y hora actual en la zona horaria local
            categoria.save()
            return redirect('administrador:productosCategorias')
    else:
        form = ProductoCategoriaAddForm()

    template = 'productosCategorias/agregar_categoria.html'
    return render(request, template, {'form': form})

@edit_categoriaProd_permission
def edit_categoriasProd(request, categoriaProd_id):
    categoria = get_object_or_404(CategoriaProd, id=categoriaProd_id)

    if request.method == 'POST':
        # Si se envió un formulario, procesa los datos
        form = ProductoCategoriaEditForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('administrador:productosCategorias')  # Redirige a la vista de posts después de la edición
    else:
        # Si es una solicitud GET, muestra el formulario de edición
        form = ProductoCategoriaEditForm(instance=categoria)

    return render(request, 'productosCategorias/editar_categoria.html', {'form': form, 'categoria': categoria})



#Trabajando con grupos
def grupos(request):

    # Obtener todos los grupos
    grupos = Group.objects.all()

    # Crear un diccionario para almacenar la información de los grupos, usuarios y permisos
    grupos_info = []

    for grupo in grupos:
        # Obtener los usuarios pertenecientes a este grupo
        usuarios = User.objects.filter(groups=grupo)

        # Obtener los permisos asignados a este grupo
        permisos = Permission.objects.filter(group=grupo)

        # Agregar la información del grupo, usuarios y permisos al diccionario
        grupo_info = {
            'grupo': grupo,
            'usuarios': usuarios,
            'permisos': permisos,
        }

        grupos_info.append(grupo_info)

    # Renderizar una plantilla con la información de los grupos, usuarios y permisos
    return render(request, 'grupos/grupos.html', {'grupos_info': grupos_info})

def unGrupo(request, grupo_id):

    # Obtener el grupo específico utilizando su ID
    grupo = get_object_or_404(Group, pk=grupo_id)

    # Obtener los usuarios que pertenecen a este grupo
    usuarios = User.objects.filter(groups=grupo)

    # Obtener los permisos asignados a este grupo
    permisos = Permission.objects.filter(group=grupo)

    # Renderizar una plantilla con la información del grupo, usuarios y permisos
    return render(request, 'grupos/unGrupo.html', {'grupo': grupo, 'usuarios': usuarios, 'permisos': permisos})

def addUsuarioGrupo(request, grupo_id):
    try:
        grupo = Group.objects.get(id=grupo_id)
    except Group.DoesNotExist:
        return HttpResponse("El grupo especificado no existe")

    # Obtén todos los usuarios que NO están en el grupo dado
    usuarios_no_en_grupo = User.objects.exclude(groups=grupo)

    if request.method == 'POST':
        # Procesar el formulario cuando se envía
        usuarios_seleccionados = request.POST.getlist('usuarios_seleccionados')
        # Agrega los usuarios seleccionados al grupo
        for usuario_id in usuarios_seleccionados:
            usuario = User.objects.get(id=usuario_id)
            grupo.user_set.add(usuario)
        return redirect('administrador:grupos')  # Redirige a donde desees después de agregar los usuarios

    context = {
        'grupo': grupo,
        'usuarios_no_en_grupo': usuarios_no_en_grupo,
    }
    return render(request, 'grupos/agregarUsuario.html', context)

def addPermisoGrupo(request, grupo_id):
    try:
        grupo = Group.objects.get(id=grupo_id)
    except Group.DoesNotExist:
        return HttpResponse("El grupo especificado no existe")

    # Obtén todos los permisos que NO están en el grupo dado
    permisos_no_en_grupo = Permission.objects.exclude(group=grupo)

    if request.method == 'POST':
        # Procesar el formulario cuando se envía
        permisos_seleccionados = request.POST.getlist('permisos_seleccionados')
        # Agrega los permisos seleccionados al grupo
        for permiso_id in permisos_seleccionados:
            permiso = Permission.objects.get(id=permiso_id)
            grupo.permissions.add(permiso)  # Usar 'permissions' en lugar de 'user_set'
        return redirect('administrador:grupos')  # Redirige a donde desees después de agregar los permisos

    context = {
        'grupo': grupo,
        'permisos_no_en_grupo': permisos_no_en_grupo,
    }
    return render(request, 'grupos/agregarPermiso.html', context)

def deleteUsuarioGrupo(request, grupo_id, user_id):
    # Obtén el grupo y el usuario o devuelve un error 404 si no existen
    grupo = get_object_or_404(Group, id=grupo_id)
    usuario = get_object_or_404(User, id=user_id)

    # Verifica si el usuario está en el grupo antes de eliminarlo
    if usuario in grupo.user_set.all():
        grupo.user_set.remove(usuario)
        return redirect('administrador:grupos')
    
    context = {
        'grupo': grupo,
        'usuario': usuario,
    }
    
    return render(request, 'grupos/eliminarUsuario.html', context)

def deletePermisoGrupo(request, grupo_id, permiso_id):
    
    # Obtén el grupo y el permiso o devuelve un error 404 si no existen
    grupo = get_object_or_404(Group, id=grupo_id)
    permiso = get_object_or_404(Permission, id=permiso_id)

    # Verifica si el permiso está en el grupo antes de eliminarlo
    if permiso in grupo.permissions.all():
        grupo.permissions.remove(permiso)
        return redirect('administrador:grupos')
    
    context = {
        'grupo': grupo,
        'permiso': permiso,
    }
    
    return render(request, 'grupos/eliminarPermiso.html', context)