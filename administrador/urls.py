from django.urls import path
from . import views

app_name = 'administrador'

urlpatterns = [

    path('usuarios/', views.user, name='usuarios'),
    path('editarUser/<int:user_id>/', views.edit_user, name='usuariosEdit'),
    path('eliminarUser/<int:user_id>/', views.delete_user, name='usuariosDelet'),
    path('agregarUser/', views.add_user, name='usuariosAdd'),

    path('roles/', views.rol, name='roles'),
    path('rolesUsuario/<int:user_id>/', views.rolUser, name='rolesUsuario'),
    path('eliminarRolesUsuario/<int:user_id>/<int:permission_id>/', views.delete_rolUser, name='rolesUsuarioDelet'),
    path('agregarRolesUsuario/<int:user_id>/', views.add_rolUser, name='rolesUsuarioAdd'),
    path('agregarRol/<int:user_id>/<int:permission_id>', views.agregarRol, name='agregarPermiso'),
    

    path('blogs/', views.blog, name='blogs'),
    path('editBlog/<int:post_id>/', views.edit_blog, name='blogEdit'),
    path('deleteBlog/<int:post_id>/', views.delete_blog, name='blogDelete'),
    path('addBlog/', views.add_blog, name='blogAdd'),

    path('blogsCategorias/', views.blogsCategorias, name='blogsCategorias'),
    path('addBlogCategoria/', views.add_blogCategoria, name='blogCategoriaAdd'),
    path('editBlogCategoria/<int:postCategoria_id>/', views.edit_blogCategoria, name='blogCategoriaEdit'),

    path('servicios/', views.servicios, name='servicios'),
    path('editServicio/<int:servicio_id>/', views.edit_servicios, name='servicioEdit'),
    path('deleteServicio/<int:servicio_id>/', views.delete_servicios, name='servicioDelete'),
    path('addServicio/', views.add_servicios, name='servicioAdd'),

    path('productos/', views.productos, name='productos'),
    path('editProducto/<int:producto_id>/', views.edit_productos, name='productoEdit'),
    path('deleteProducto/<int:producto_id>/', views.delete_productos, name='productoDelete'),
    path('addProducto/', views.add_productos, name='productoAdd'),

    path('productosCategorias/', views.categotiasProd, name='productosCategorias'),
    path('addProductosCategoria/', views.add_categoriasProd, name='productosCategoriaAdd'),
    path('editProductosCategoria/<int:categoriaProd_id>/', views.edit_categoriasProd, name='productosCategoriaEdit'),

    path('grupos/', views.grupos, name='grupos'),
    path('unGrupo/<int:grupo_id>/', views.unGrupo, name='traerObjetosDeGrupo'),
    path('agregarUsuario/<int:grupo_id>/', views.addUsuarioGrupo, name='agregarUsuario'),
    path('agregarPermiso/<int:grupo_id>/', views.addPermisoGrupo, name='agregarPermiso'),
    path('eliminarUsuario/<int:grupo_id>/<int:user_id>/', views.deleteUsuarioGrupo, name='eliminarUsuario'),
    path('eliminarPermiso/<int:grupo_id>/<int:permiso_id>/', views.deletePermisoGrupo, name='eliminarPermiso'),
    
    
      
]
