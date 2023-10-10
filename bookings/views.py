from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Appointment
from .models import Treatment


# Create your views here.
def appointment_set(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('bookings:appointment_list')

    context = {'form': form}
    return render(request, 'bookings/appointment_set.html', context)


def appointment_list(request):
    appointment_list = Appointment.objects.all()
    template_name = 'bookings/appointment_list.html'
    context = {'appointment_list': appointment_list}
    return render(request, template_name, context)
