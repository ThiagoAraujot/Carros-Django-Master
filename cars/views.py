from django.shortcuts import render

# Create your views here.


def car_view(request):
    return render(
        request,
        'cars.html',
        {'cars': {'model': 'Porsche GT3 RS'}}
    )
