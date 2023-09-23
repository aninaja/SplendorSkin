from django.shortcuts import render
from .models import CustomUser
from .forms import RegistrationForm


# Create your views here.


def account_create(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        form = RegistrationForm()
    template_name = 'accounts/account_create.html'
    context = {'form': form}
    return render(request, template_name, context)
