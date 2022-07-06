from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('keyboards/', views.keyboards_index, name='keyboards'),
    path('keyboards/<int:keyboard_id>', views.keyboard_detail, name='detail'),
    path('keyboards/create/', views.KeyboardCreate.as_view(), name='keyboard_create'),
    path('keyboards/<int:pk>/update/', views.KeyboardUpdate.as_view(), name='keyboard_update'),
    path('keyboards/<int:pk>/delete/', views.KeyboardDelete.as_view(), name='keyboard_delete'),
    path('keyboards/<int:keyboard_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]