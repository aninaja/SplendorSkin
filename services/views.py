from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ServiceForm, TreatmentForm, AreaForm, TypeForm
from .models import Service, Treatment, TreatmentArea, PriceType
from django.contrib import messages


# Create your views here.
def service_list(request):
    service_list = Service.objects.exclude(status='Deleted')
    template_name = 'services/service_list.html'
    context = {'service_list': service_list}
    return render(request, template_name, context)


def service_create(request):
    form = ServiceForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Service created successfully.')
        return redirect('services:service_list')
    template_name = 'services/service_create.html'
    context = {'form': form}
    return render(request, template_name, context)


def service_edit(request, pk):
    service = get_object_or_404(Service, id=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Service updated successfully.')
        return redirect('services:service_list')
    template_name = 'services/service_edit.html'
    context = {'service': service, 'form': form}
    return render(request, template_name, context)


def service_delete(request, pk):
    service = get_object_or_404(Service, id=pk)
    service.status = 'Deleted'
    service.save()
    messages.success(request,
                     'Service has been marked as "Deleted".')
    return redirect('services:treatment_list')


def treatment_area_list(request):
    treatment_area_list = TreatmentArea.objects.exclude(status='Deleted')
    template_name = 'services/treatedarea_list.html'
    context = {'area_list': treatment_area_list}
    return render(request, template_name, context)


def treatment_area_create(request):
    form = AreaForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Treatment area created successfully.')
        return redirect('services:treatment_area_list')
    template_name = 'services/treatedarea_create.html'
    context = {'form': form}
    return render(request, template_name, context)


def treatment_area_edit(request, pk):
    treatment_area = get_object_or_404(TreatmentArea, id=pk)
    form = AreaForm(request.POST or None, instance=treatment_area)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Treatment area updated successfully.')
        return redirect('services:treatment_area_list')
    template_name = 'services/treatedarea_edit.html'
    context = {'area': treatment_area, 'form': form}
    return render(request, template_name, context)


def treatment_area_delete(request, pk):
    treatment_area = get_object_or_404(TreatmentArea, id=pk)
    treatment_area.status = 'Deleted'
    treatment_area.save()
    messages.success(request,
                     'Treatment area has been marked as deleted.')
    return redirect('services:treatment_area_delete')


def price_type_list(request):
    pricing_type_list = PriceType.objects.exclude(status='Deleted')
    template_name = 'services/pricetype_list.html'
    context = {'ptype_list': pricing_type_list}
    return render(request, template_name, context)


def price_type_create(request):
    form = TypeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Price type created successfully.')
        return redirect('services:price_type_list')
    template_name = 'services/pricetype_create.html'
    context = {'form': form}
    return render(request, template_name, context)


def price_type_edit(request, pk):
    price_type = get_object_or_404(PriceType, id=pk)
    form = TypeForm(request.POST or None, instance=price_type)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Price type updated successfully.')
        return redirect('services:price_type_list')
    template_name = 'services/pricetype_edit.html'
    context = {'price_type': price_type, 'form': form}
    return render(request, template_name, context)


def price_type_delete(request, pk):
    price_type = get_object_or_404(PriceType, id=pk)
    price_type.status = 'Deleted'
    price_type.save()
    messages.success(request,
                     'Price type has been marked as deleted.')
    return redirect('services:price_type_list')
    template_name = 'services/pricetype_list.html'
    context = {'price_type': price_type}
    return render(request, template_name, context)


def treatment_list(request):
    treatment_list = Treatment.objects.exclude(status='Deleted')
    template_name = 'services/treatment_list.html'
    context = {'treatment_list': treatment_list}
    return render(request, template_name, context)


def treatment_create(request):
    form = TreatmentForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Treatment created successfully.')
        return redirect('services:treatment_list')
    template_name = 'services/treatment_create.html'
    context = {'form': form}
    return render(request, template_name, context)


def treatment_edit(request, pk):
    treatment = get_object_or_404(Treatment, id=pk)
    form = TreatmentForm(request.POST or None, instance=treatment)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Treatment created successfully.')
        return redirect('services:treatment_list')
    template_name = 'services/treatment_edit.html'
    context = {'form': form, 'treatment': treatment}
    return render(request, template_name, context)


def treatment_delete(request, pk):
    treatment = get_object_or_404(Treatment, id=pk)
    treatment.status = 'Deleted'
    treatment.save()
    messages.success(request,
                     'Treatment has been marked as deleted.')
    return redirect('services:treatment_list')
