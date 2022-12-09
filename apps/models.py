from django.db import models

class Tarefas(models.Model):
    tarefa = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tarefa