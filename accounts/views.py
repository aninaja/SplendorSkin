from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def account_list(request):
    users = CustomUser.objects.all()
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
    form = RegistrationForm(request.POST or None, intance=CustomUser)
    if form.is_valid():
        form.save()
    template_name = 'accounts/account_edit.html'
    context = {'users': users, 'form': form}
    return render(request, template_name, context)


def loginview(request):
    return render(request, 'accounts/login.html')


def process_login(request):
    mobile = request.POST.get('username')
    password = request.POST.get('password')

    # Check if the mobile number exists and if the expected password matches
    user = authenticate(request, username=mobile, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/accounts/list')
    else:
        return render(request, 'accounts/login.html', {
            'error_message': "Login Failed"
        })


def process_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
