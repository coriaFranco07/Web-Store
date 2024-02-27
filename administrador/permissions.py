from django.contrib.auth.decorators import permission_required

# Permisos usuarios
view_user_permission = permission_required("auth.view_user", raise_exception=True)
edit_user_permission = permission_required("auth.change_user", raise_exception=True)
delete_user_permission = permission_required("auth.delete_user", raise_exception=True)
add_user_permission = permission_required("auth.add_user", raise_exception=True)

# Roles
view_rol_permission = permission_required("auth.view_permission", raise_exception=True)
add_rol_permission = permission_required("auth.add_permission", raise_exception=True)
delete_rol_permission = permission_required("auth.delete_permission", raise_exception=True)


#Post
view_post_permission = permission_required("auth.view_post", raise_exception=True)
edit_post_permission = permission_required("auth.change_post", raise_exception=True)
delete_post_permission = permission_required("auth.delete_post", raise_exception=True)
add_post_permission = permission_required("auth.add_post", raise_exception=True)


#Post Categorias
view_categoria_permission = permission_required("auth.view_categoria", raise_exception=True)
edit_categoria_permission = permission_required("auth.change_categoria", raise_exception=True)
add_categoria_permission = permission_required("auth.add_categoria", raise_exception=True)


#Servivios
view_servicio_permission = permission_required("auth.view_servicio", raise_exception=True)
edit_servicio_permission = permission_required("auth.change_servicio", raise_exception=True)
delete_servicio_permission = permission_required("auth.delete_servicio", raise_exception=True)
add_servicio_permission = permission_required("auth.add_servicio", raise_exception=True)


#Productos
view_producto_permission = permission_required("auth.view_producto", raise_exception=True)
edit_producto_permission = permission_required("auth.change_producto", raise_exception=True)
delete_producto_permission = permission_required("auth.delete_producto", raise_exception=True)
add_producto_permission = permission_required("auth.add_producto", raise_exception=True)


#Categoria Categorias
view_categoriaProd_permission = permission_required("auth.view_categoriaProd", raise_exception=True)
edit_categoriaProd_permission = permission_required("auth.change_categoriaProd", raise_exception=True)
add_categoriaProd_permission = permission_required("auth.add_categoriaProd", raise_exception=True)




