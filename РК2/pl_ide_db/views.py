from django.shortcuts import render
from .models import IDE, Lang
# Create your views here.

def IDELangs(request):
    langs = Lang.objects.all()
    ides = IDE.objects.all()
    context = {
        'langs': langs,
        'ides': ides
    }
    return render(request, 'base.html', context)