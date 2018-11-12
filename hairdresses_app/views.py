from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from hairdresses_app.forms import ClientForm, HairdoForm, AdditionalSetviceForm, BillForm
from hairdresses_app.models import Client, Hairdo, AdditionalService, Bill


def list_of_clients(request):
    context = {'form': ClientForm()}
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        sex = request.POST.get('sex')
        sign_regular_customer = bool(request.POST.get('sign_regular_customer'))
        client = Client.objects.create(name=name, surname=surname, sex=sex, sign_regular_customer=sign_regular_customer)
    context['clients'] = Client.objects.all()
    return render(request, 'hairdresses_app/clients.html', context)


def list_of_hairstyles(request):
    context = {'form': HairdoForm()}
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        sex = request.POST.get('sex')
        hairdo = Hairdo.objects.create(name=name, price=price, sex=sex)
    context['hairstyles'] = Hairdo.objects.all()
    return render(request, 'hairdresses_app/hairstyles.html', context)


def list_of_additional_services(request):
    context = {'form': AdditionalSetviceForm()}
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        additional_service = AdditionalService.objects.create(name=name, price=price)
    context['additional_services'] = AdditionalService.objects.all()
    return render(request, 'hairdresses_app/additional_services.html', context)


def list_of_bills(request):
    context = {
        'clients': Client.objects.all(),
        'hirestyles': Hairdo.objects.all(),
        'add_servs': AdditionalService.objects.all(),
    }
    if request.POST:
        try:
            client = Client.objects.get(pk=int(request.POST.get('client_id')))
            hairdo = Hairdo.objects.get(pk=int(request.POST.get('hairdo_id')))
            additional_service = AdditionalService.objects.filter(
                pk__in=request.POST.getlist('additional_services_ids'))
            bill = Bill.objects.create(client=client, hairdo=hairdo)
            for add_sev in additional_service:
                bill.additional_services.add(add_sev)
            bill.save()
        except Client.DoesNotExist:
            return JsonResponse({"error": "client not found"})
        except Hairdo.DoesNotExist:
            return JsonResponse({"error": "hairdo not found"})
    context['bills'] = Bill.objects.all()
    return render(request, 'hairdresses_app/bills.html', context)


class ClientView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/client_detail.html',
            {'client': Client.objects.get(pk=kwargs.get('pk'))}
        )


@method_decorator(csrf_exempt, name='dispatch')
class ClientUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/client_update.html',
            {'form': ClientForm(instance=Client.objects.get(pk=kwargs.get('pk')))}
        )

    def post(self, request, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('pk'))
        client.name = request.POST.get('name')
        client.surname = request.POST.get('surname')
        client.sex = request.POST.get('sex')
        client.sign_regular_customer = bool(request.POST.get('sign_regular_customer'))
        client.save()
        return render(request, 'hairdresses_app/client_update.html', {'form': ClientForm(instance=client)})

    def delete(self, request, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('pk'))
        client.delete()
        return redirect('list-of-clients')


class HairdoView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/hairdo_detail.html',
            {'hairdo': Hairdo.objects.get(pk=kwargs.get('pk'))}
        )


@method_decorator(csrf_exempt, name='dispatch')
class HairdoUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/hairdo_update.html',
            {'form': HairdoForm(instance=Hairdo.objects.get(pk=kwargs.get('pk')))}
        )

    def post(self, request, *args, **kwargs):
        hairdo = Hairdo.objects.get(pk=kwargs.get('pk'))
        hairdo.name = request.POST.get('name')
        hairdo.price = float(request.POST.get('price'))
        hairdo.sex = request.POST.get('sex')
        hairdo.save()
        return render(request, 'hairdresses_app/hairdo_update.html', {'form': HairdoForm(instance=hairdo)})

    def delete(self, request, *args, **kwargs):
        hairdo = Hairdo.objects.get(pk=kwargs.get('pk'))
        hairdo.delete()
        return redirect('list-of-hairstyles')


class AdditionalServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/additional_service_detail.html',
            {'additional_service': AdditionalService.objects.get(pk=kwargs.get('pk'))}
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdditionalServiceUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/additional_service_update.html',
            {'form': AdditionalSetviceForm(instance=AdditionalService.objects.get(pk=kwargs.get('pk')))}
        )

    def post(self, request, *args, **kwargs):
        additional_service = AdditionalService.objects.get(pk=kwargs.get('pk'))
        additional_service.name = request.POST.get('name')
        additional_service.price = float(request.POST.get('price'))
        additional_service.save()
        return render(
            request,
            'hairdresses_app/additional_service_update.html',
            {'form': AdditionalSetviceForm(instance=additional_service)}
        )

    def delete(self, request, *args, **kwargs):
        additional_service = AdditionalService.objects.get(pk=kwargs.get('pk'))
        additional_service.delete()
        return redirect('list-of-additional-services')


class CliendDeleteView(View):
    def post(self, request, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('pk'))
        client.delete()
        return JsonResponse({'status': 'OK'})


class HairdoDeleteView(View):
    def post(self, request, *args, **kwargs):
        hairdo = Hairdo.objects.get(pk=kwargs.get('pk'))
        hairdo.delete()
        return JsonResponse({'status': 'OK'})


class AdditionalServiceView(View):
    def post(self, request, *args, **kwargs):
        additional_service = AdditionalService.objects.get(pk=kwargs.get('pk'))
        additional_service.delete()
        return JsonResponse({'status': 'OK'})


class BillView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/bill_detail.html',
            {'bill': Bill.objects.get(pk=kwargs.get('pk'))}
        )

@method_decorator(csrf_exempt, name='dispatch')
class BillUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'hairdresses_app/bill_update.html',
            {'form': BillForm(instance=Bill.objects.get(pk=kwargs.get('pk')))}
        )

    def post(self, request, *args, **kwargs):
        bill = Bill.objects.get(pk=kwargs.get('pk'))
        bill.client.name = request.POST.get('name')
        bill.client.surname = request.POST.get('surname')
        bill.hairdo.name = request.POST.get('name')
        bill.additional_services.name = request.POST.get('additional_services')
        bill.date = request.POST.get('date')
        bill.total_sum = request.POST.get('total_sum')
        bill.save()
        return render(request, 'hairdresses_app/bill_update.html', {'form': BillForm(instance=bill)})

    def delete(self, request, *args, **kwargs):
        bill = Bill.objects.get(pk=kwargs.get('pk'))
        bill.delete()
        return redirect('list-of-bills')