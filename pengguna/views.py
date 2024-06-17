from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from pengguna.forms import (UserDetailForm, UserEditFormDB, UserEditForm, BiodataForm)
from pengguna.models import Biodata

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def pengguna_list(request):
    template_name = "dashboard/snippets/pengguna/pengguna_list.html"
    users = User.objects.all()
    context = {
        'title' : 'Selamat Datang Di Web Saya',
        'users' : users,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def pengguna_detail(request, id_user):
    template_name = "dashboard/snippets/pengguna/pengguna_detail.html"
    user = User.objects.get(id=id_user)
    form = UserDetailForm(instance=user)  # Inisialisasi form dengan instance user

    context = {
        'title': 'Detail User',
        'form': form,  # Mengirimkan form ke template
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def pengguna_edit(request, id_user):
    template_name = "dashboard/snippets/pengguna/pengguna_edit.html"
    user = User.objects.get(id=id_user)
    if request.method == 'POST':
        form = UserEditFormDB(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()  # To save the groups
            messages.success(request, 'User updated successfully!')
            return redirect('pengguna_list')
    else:
        form = UserEditFormDB(instance=user)

        context = {
        'title': 'Edit User',
        'form': form
    }
        
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator, login_url='/authentikasi/logout')
def pengguna_delete(request, id_user):
    try:
        user = User.objects.get(id=id_user)
        if request.user.groups.filter(name='Operator'):
            pass
        else:
            if user.author != request.user:
                return redirect ('home')
        user.delete()
    except:
        pass
    return redirect(pengguna_list)

@login_required
def user_profile(request):
    template_name = "halaman/profile.html"
    user = request.user
    biodata = Biodata.objects.get(user=user)
    
    context = {
        'user': user,
        'biodata': biodata,
    }
    return render(request, template_name, context)

@login_required
def edit_profile(request):
    template_name = "halaman/edit_profile.html"
    user = request.user
    try:
        biodata = Biodata.objects.get(user=user)
    except Biodata.DoesNotExist:
        biodata = Biodata(user=user)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        biodata_form = BiodataForm(request.POST, request.FILES, instance=biodata)
        
        if user_form.is_valid() and biodata_form.is_valid():
            user_form.save()
            biodata_form.save()
            return redirect('profile')  # Ganti 'profile' dengan nama URL yang sesuai untuk profil pengguna
        
    else:
        user_form = UserEditForm(instance=user)
        biodata_form = BiodataForm(instance=biodata)
    
    context = {
        'user_form': user_form,
        'biodata_form': biodata_form,
    }

    return render(request, template_name, context
        )