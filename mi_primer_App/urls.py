from django.urls import path
from .views import (inicio,about, CursoCreateView, EstudianteCreateView, 
                    buscar_curso, CursoListView, EntregableCreateView, EstudianteListView,
                    EntregableListView, CursoDetailView, CursoUpdateView, CursoDeleteView, 
                    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView, 
                    EntregableDetailView, EntregableUpdateView, EntregableDeleteView, 
                    buscar_entregable)

urlpatterns = [
    path('', inicio, name='inicio'),  
    path('crear-curso/', CursoCreateView.as_view(), name='crear-curso'),
    path('cursos/', CursoListView.as_view(), name='cursos'),
    path('detalles-curso/<int:pk>', CursoDetailView.as_view(),name='curso-detail'),
    path('actualizar-curso/<int:pk>', CursoUpdateView.as_view(),name='curso-update'),
    path('eliminar-curso/<int:pk>', CursoDeleteView.as_view(),name='curso-delete'),
    path('buscar-cursos/', buscar_curso, name='buscar-cursos'),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name='crear-estudiante'),
    path('estudiantes/', EstudianteListView.as_view(), name='estudiantes'),
    path('detalles-estudiante/<int:pk>', EstudianteDetailView.as_view(),name='estudiante-detail'),
    path('actualizar-estudiante/<int:pk>', EstudianteUpdateView.as_view(),name='estudiante-update'),
    path('eliminar-estudiante/<int:pk>', EstudianteDeleteView.as_view(),name='estudiante-delete'),
    path('crear-entregable/', EntregableCreateView.as_view(), name='crear-entregable'),
    path('listas-entregables/', EntregableListView.as_view(), name='entregables'),
    path('detalles-entrega/<int:pk>', EntregableDetailView.as_view(),name='entrega-detail'),
    path('actualizar-entrega/<int:pk>', EntregableUpdateView.as_view(),name='entrega-update'),
    path('eliminar-entrega/<int:pk>', EntregableDeleteView.as_view(),name='entrega-delete'),
    path('buscar-entregable/', buscar_entregable, name='buscar-entregable'),
]


