from django.urls import path
from pengguna.views import (
    pengguna_list, pengguna_detail, pengguna_delete, 
    pengguna_edit, user_profile, edit_profile
    )

urlpatterns = [
    path('pengguna/list/', pengguna_list, name='pengguna_list'),
    path('pengguna/detail/<int:id_user>', pengguna_detail, name="pengguna_detail"),
    path('pengguna/delete/<int:id_user>', pengguna_delete, name='pengguna_delete'),
    path('pengguna/edit/<int:id_user>',  pengguna_edit, name='pengguna_edit'),
    path('profile/', user_profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
