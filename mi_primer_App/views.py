from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Entregable
from .forms import CursoForm, EstudianteForm, EntregableForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_App/inicio.html')

def about(request):
    return render(request, 'mi_primer_App/about.html')

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'mi_primer_App/crear_curso.html'
    success_url = reverse_lazy('cursos')

class CursoListView(ListView):
    model = Curso
    template_name = 'mi_primer_App/cursos.html'
    context_object_name = 'cursos'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'mi_primer_App/detalle_curso.html'
    context_object_name = 'curso'

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'mi_primer_App/crear_curso.html'
    success_url = reverse_lazy('cursos')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'mi_primer_App/eliminar_curso.html'
    success_url = reverse_lazy('cursos')

# def crear_curso(request):
#     if request.method == 'POST':
#         form = CursoForm(request.POST)
#         if form.is_valid():
#             # Procesar el formulario y guardar el curso
#             nuevo_curso = Curso(
#                 nombre=form.cleaned_data['nombre'],
#                 descripcion=form.cleaned_data['descripcion'],
#                 duracion_semanas=form.cleaned_data['duracion_semanas'],
#                 fecha_inicio=form.cleaned_data['fecha_inicio'],
#                 activo=form.cleaned_data['activo']
#             )
#             nuevo_curso.save()
#             return redirect('cursos')
#     else:
#         form = CursoForm()
#         return render(request, 'mi_primer_App/crear_curso.html', {'form': form})

class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'mi_primer_App/crear_estudiante.html'
    success_url = reverse_lazy('estudiantes')

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'mi_primer_App/estudiantes.html'
    context_object_name = 'estudiantes'

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'mi_primer_App/detalle_estudiante.html'
    context_object_name = 'estudiante'

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'mi_primer_App/crear_estudiante.html'
    success_url = reverse_lazy('estudiantes')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'mi_primer_App/eliminar_estudiante.html'
    success_url = reverse_lazy('estudiantes')

# def crear_estudiante(request):
#     if request.method == 'POST':
#         form = EstudianteForm(request.POST)
#         if form.is_valid():
#             # Procesar el formulario y guardar el curso
#             nuevo_curso = Estudiante(
#                 nombre=form.cleaned_data['nombre'],
#                 apellido=form.cleaned_data['apellido'],
#                 email=form.cleaned_data['email'],
#                 edad=form.cleaned_data['edad'],
#                 fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
#             )
#             nuevo_curso.save()
#             return redirect('inicio')
#     else:
#         form = EstudianteForm()
#         return render(request, 'mi_primer_App/crear_estudiante.html', {'form': form})

# def estudiantes(request):
#     estudiantes = Estudiante.objects.all()
#     return render(request, 'mi_primer_App/estudiantes.html', {'estudiantes': estudiantes})


# def cursos(request):
#     cursos = Curso.objects.all()
#     return render(request, 'mi_primer_App/cursos.html', {'cursos': cursos})

def buscar_curso(request):
    nombre = request.GET.get('nombre', '')
    if nombre:
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    else:
        cursos = Curso.objects.all()
    return render(request, 'mi_primer_App/cursos.html', context={'cursos': cursos,})

# def buscar_cursos(request):
#     if request.method == 'GET':
#         nombre = request.GET.get('nombre', '')
#         cursos = Curso.objects.filter(nombre__icontains=nombre)
#         return render(request, 'mi_primer_App/cursos.html', {'cursos': cursos, 'nombre': nombre})

class EntregableCreateView(CreateView):
    model = Entregable
    form_class = EntregableForm
    template_name = 'mi_primer_App/crear_entregable.html'
    success_url = reverse_lazy('entregables')

class EntregableListView(ListView):
    model = Entregable
    template_name = 'mi_primer_App/entregables.html'
    context_object_name = 'entregable'

class EntregableDetailView(DetailView):
    model = Entregable
    template_name = 'mi_primer_App/detalle_entregable.html'
    context_object_name = 'entregable'

class EntregableUpdateView(UpdateView):
    model = Entregable
    form_class = EntregableForm
    template_name = 'mi_primer_App/crear_entregable.html'
    success_url = reverse_lazy('entregables')

class EntregableDeleteView(DeleteView):
    model = Entregable
    template_name = 'mi_primer_App/eliminar_entregable.html'
    success_url = reverse_lazy('entregables')
    
def buscar_entregable(request):
    nombre = request.GET.get('nombre', '')
    if nombre:
        nombre = request.GET.get('nombre', '')
        entregable = Entregable.objects.filter(nombre__icontains=nombre)
    else:
        entregable = Entregable.objects.all()
    return render(request, 'mi_primer_App/entregables.html', context={'entregable': entregable,})

# def crear_entregable(request):
#     if request.method == 'POST':
#         form = EntregableForm(request.POST)
#         if form.is_valid():
#             # Procesar el formulario y guardar el entregable
#             nuevo_entregable = Entregable(
#                 nombre = form.cleaned_data['nombre'],
#                 fecha_entrega = form.cleaned_data['fecha_entrega'],
#                 entregado = form.cleaned_data['entregado'],
#                 estudiante = form.cleaned_data['estudiante']
#             )
#             nuevo_entregable.save()
#             return redirect('inicio')
            
#     else:
#         form = EntregableForm()
#         form.fields['estudiante'].queryset = Estudiante.objects.all()
#     return render(request, 'mi_primer_App/crear_entregable.html', {'form': form})

