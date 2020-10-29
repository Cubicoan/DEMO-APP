from django.shortcuts import render, redirect
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


def moveOneToTwo(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage2'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveTwoToOne(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage1'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveTwoToThree(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage3'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveThreeToTwo(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage2'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveThreeToFour(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage4'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveFourToThree(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage3'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveFourToFive(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage5'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')


def moveFiveToFour(request, pk):
    task = Task.objects.get(sub_task_no=pk)
    if request.method == 'POST':
        task.stage = 'stage4'
        task.save(update_fields=['stage'])

        return redirect("index")

    return render(request, 'index.html')
