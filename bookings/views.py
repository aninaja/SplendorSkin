from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Appointment
from .models import Treatment


# Create your views here.
def set_appointment(request):
    treatment_instance = get_object_or_404(Treatment)
    form = BookingForm(request.POST or None, initial={'treatment': treatment_instance})
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            return redirect('bookings:appointment_list')

    context = {'form': form, 'treatment_instance': treatment_instance}
    return render(request, 'bookings/booking_create.html', context)


def appointment_list(request):
    appointment_list = Appointment.objects.all()
    template_name = 'bookings/appointment_list.html'
    context = {'appointment_list': appointment_list}
    return render(request, template_name, context)
