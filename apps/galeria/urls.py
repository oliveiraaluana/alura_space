from django.urls import path
from apps.galeria.views import \
      index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path("nova-Imagem", nova_imagem, name="nova_imagem"),
    path("editar-Imagem", editar_imagem, name="editar_imagem"),
    path("deletar-Imagem", deletar_imagem, name="deletar_imagem"),
]