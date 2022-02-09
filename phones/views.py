from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', None)
    if sort is None:
        phones = Phone.objects.all()
    if sort == 'max_price':
        phones = Phone.objects.order_by('-price')
        print(phones)
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'name':
        phones = Phone.objects.order_by('name')


    template = 'catalog.html'

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        context = {'phone': phone}
    template = 'product.html'
    return render(request, template, context)
