from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def account_list(request):
    users = CustomUser.objects.exclude(status='Deleted')
    template_name = 'accounts/account_list.html'
    context = {'users': users}
    return render(request, template_name, context)


def account_create(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Account updated successfully.')
        return redirect('accounts:account_list')
    template_name = 'accounts/account_create.html'
    context = {'form': form}
    return render(request, template_name, context)


def account_edit(request, pk):
    users = get_object_or_404(CustomUser, id=pk)
    form = RegistrationForm(request.POST or None, instance=users)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'User account updated successfully.')
        return redirect('accounts:account_list')

    template_name = 'accounts/account_edit.html'
    context = {'users': users, 'form': form}
    return render(request, template_name, context)


def account_delete(request, pk):
    users = get_object_or_404(CustomUser, id=pk)
    users.status = 'Deleted'
    users.save()
    messages.success(request,
                     'User account has been deleted')
    return redirect('accounts:account_list')

