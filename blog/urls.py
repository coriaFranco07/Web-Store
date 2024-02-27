from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.post, name="Blog"),
    path('categoria/<categoria_id>/', views.categoria, name="categoria")
 
]