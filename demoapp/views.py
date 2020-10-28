from django.shortcuts import render
from .models import *


# Create your views here.

def IndexPage(request):
    stage1 = Task.objects.filter(stage='stage1')
    stage2 = Task.objects.filter(stage='stage2')
    stage3 = Task.objects.filter(stage='stage3')
    stage4 = Task.objects.filter(stage='stage4')
    stage5 = Task.objects.filter(stage='stage5')

    context = {'stage1': stage1, 'stage2': stage2, 'stage3': stage3, 'stage4': stage4, 'stage5': stage5}
    return render(request, 'index.html', context)
