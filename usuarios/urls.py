from django.urls import path

from .views import UserRegisterView, CustomLoginView, CustomLogoutView, ProfileView, AvatarUpdateView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('perfil/', ProfileView.as_view(), name='perfil'),
    path("editar-perfil/", ProfileUpdateView.as_view(), name="editar_perfil"),
    path('update-avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]