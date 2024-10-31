# admin_dashboard/views.py

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserProfileForm
from .models import UserProfile


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'admin_dashboard/user_list.html', {'users': users})


@login_required
@user_passes_test(is_admin)
def add_user(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = User()
    users = User.objects.all()
    return render(request, 'admin_dashboard/add_user.html', {'form': form, 'users': users})


@login_required
@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    if request.method == "POST":
        UserProfile.objects.filter(id=user_id).update(login_count=request.POST.get(
            'login_count'), chat_count=request.POST.get('chat_count'))
        return redirect('user_list')
    else:
        form = UserProfileForm(instance=user)
    users = User.objects.all()
    return render(request, 'admin_dashboard/edit_user.html', {'form': form, 'users': users})


@login_required
@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')
