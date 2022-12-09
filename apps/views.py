from django.shortcuts import render, redirect
from .models import Tarefas

def index(request):
    tarefas = Tarefas.objects.all()
    return render(request,"index.html", {"tarefas": tarefas})

def save(request):
    tarefas1 = request.POST.get("tarefas")
    if not tarefas1.strip():
        return redirect(index)

    Tarefas.objects.create(tarefa=tarefas1)
    return redirect(index)

def status(request, id):
    pessoa = Tarefas.objects.get(id=id)
    return render(request,"status.html", {"pessoa": pessoa})


def atualizar(request, id):
    tarefas1 = request.POST.get("tarefas")
    pessoa = Tarefas.objects.get(id=id)
    pessoa.tarefa = tarefas1
    pessoa.save()
    return redirect(index)

def apagar(request, id):
    pessoa = Tarefas.objects.get(id=id)
    pessoa.delete()
    return redirect(index)