from django.shortcuts import render, get_object_or_404
from .models import Bungalov, Villa
from .forms import BungalovForm, BungalovImageForm

def index(request):
    villas = Villa.objects.all()
    bungalovs = Bungalov.objects.all()
    return render(request, 'index.html', {'bungalovs': bungalovs, 'villas': villas})

def bungalov(request):
    bungalovs = Bungalov.objects.all()
    return render(request, 'bungalov.html', {'bungalovs': bungalovs})

def bungalov_detail(request, pk):
    bungalov = get_object_or_404(Bungalov, pk=pk)
    images = bungalov.images.all()
    return render(request, 'bungalov_detail.html', {'bungalov': bungalov, 'images': images})

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def gizlilik(request):
    return render(request, 'gizlilik.html')

def kurallar(request):
    kurallar = Kurallar.objects.all()
    return render(request, 'kurallar.html', {'kurallar': kurallar})

def villa(request):
    villas = Villa.objects.all()
    return render(request, 'villa.html', {'villas': villas})

def villa_detail(request, id):
    villa = get_object_or_404(Villa, id=id)
    images = villa.images.all()
    return render(request, 'villa_detail.html', {'villa': villa, 'images': images})
def belgeler(request):
    return render(request, 'belgeler.html')
